frappe.pages['quiz'].on_page_load = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Quiz',
		single_column: true
	});

	wrapper.quiz = new Quiz(wrapper);
};

class Quiz {
	constructor(wrapper) {
		this.page = wrapper.page;
		this.wrapper = wrapper;
		this.current_question_index = 0;
		this.questions = [];
		this.score = 0;

		this.get_questions();
	}

	get_questions() {
		frappe.call({
			method: 'frappe.client.get_list',
			args: {
				doctype: 'Quiz',
				fields: ['name', 'question', 'options', 'correct_answer'],
				limit_page_length: 10
			},
			callback: (r) => {
				if (!r.exc && r.message) {
					this.questions = r.message;
					this.render_question();
				}
			}
		});
	}

	render_question() {
		if (this.current_question_index < this.questions.length) {
			const question = this.questions[this.current_question_index];
			const options = JSON.parse(question.options);

			const html = `
				<h3>${question.question}</h3>
				<div id="options">
					${options.map((option, index) => `<div><input type="radio" name="option" value="${index}">${option}</div>`).join('')}
				</div>
				<button onclick="quiz.submit_answer()">Submit</button>
			`;

			this.page.set_content(html);
		} else {
			this.show_score();
		}
	}

	submit_answer() {
		const selected_option = document.querySelector('input[name="option"]:checked');
		if (!selected_option) {
			frappe.msgprint('Please select an option');
			return;
		}

		const question = this.questions[this.current_question_index];
		const selected_option_index = parseInt(selected_option.value);
		const correct_answer_index = parseInt(question.correct_answer);

		if (selected_option_index === correct_answer_index) {
			this.score += 2;
		}

		this.current_question_index++;
		this.render_question();
	}

	show_score() {
		const html = `<h3>Your score: ${this.score}</h3>`;
		this.page.set_content(html);
	}
}
