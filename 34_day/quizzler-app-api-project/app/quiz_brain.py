import html

class QuizBrain:
    """A classe QuizBrain é responsável por gerenciar a lógica do quiz, incluindo o rastreamento de perguntas, pontuação e verificação de respostas."""

    def __init__(self, q_list):
        """ 
        Inicializa o QuizBrain com uma lista de perguntas.
        args:
            q_list: Lista de objetos de perguntas, onde cada objeto contém o texto da pergunta e a resposta correta.
        """

        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None


    def still_has_questions(self):
        """Verifica se ainda há perguntas restantes na lista de perguntas."""

        return self.question_number < len(self.question_list)


    def next_question(self):
        """Retorna a próxima pergunta da lista de perguntas e incrementa o número da pergunta atual."""

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer):
        """Verifica se a resposta do usuário está correta em relação à resposta da pergunta atual.
        args:
            user_answer: A resposta fornecida pelo usuário.
        Returns:
            True se a resposta estiver correta, False caso contrário.
        """
        
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
