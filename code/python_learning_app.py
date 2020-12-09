"""
This file contains code for the application "Python Learning App".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary libraries


import sys
import copy
import pickle
import os


# Creating static functions


def load_question_list(file_name):
    # type: (str) -> QuestionList
    return pickle.load(open(file_name, "rb"))


def save_question_list(question_list, file_name):
    # type: (QuestionList, str) -> None
    pickle.dump(question_list, open(file_name, "wb"))


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Importing necessary class


class Question:
    """
    This class contains attributes of a question asked in the application.
    """

    def __init__(self, question):
        # type: (str) -> None
        self.question: str = question
        self.__answers: list = []  # initial value

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += str(self.question) + "\n"
        res += "Answers:\n"
        answer_count: int = 1
        for answer in self.__answers:
            res += "#" + str(answer_count) + ". " + str(answer) + "\n"
            answer_count += 1

        return res

    def get_answers(self):
        # type: () -> list
        return self.__answers

    def add_answer(self, answer):
        # type: (str) -> None
        self.__answers.append(answer)

    def remove_answer(self, answer):
        # type: (str) -> bool
        if answer in self.__answers:
            self.__answers.remove(answer)
            return True
        return False

    def clone(self):
        # type: () -> Question
        return copy.deepcopy(self)


class QuestionList:
    """
    This class contains attributes of a list of questions.
    """

    def __init__(self, questions=None):
        # type: (list) -> None
        if questions is None:
            questions = []

        self.__questions: list = questions

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        for question in self.__questions:
            res += str(question) + "\n"

        return res

    def add_question(self, question):
        # type: (str) -> None
        self.__questions.append(Question(question))

    def remove_question(self, question):
        # type: (Question) -> bool
        if question in self.__questions:
            self.__questions.remove(question)
            return True
        return False

    def get_questions(self):
        # type: () -> list
        return self.__questions

    def clone(self):
        # type: () -> QuestionList
        return copy.deepcopy(self)


# Creating main function used to run the application.


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'Python Learning App' by 'DtjiSoftwareDeveloper'.")
    print("This application allows you to ask Python programming language-related questions and get answers.")
    print("All indices in this app start from 1.")

    # Automatically load saved question list
    file_name: str = "SAVED QUESTION LIST"
    new_question_list: QuestionList
    try:
        new_question_list = load_question_list(file_name)

        # Clearing up the command line window
        clear()

        print("Below is a list of questions and answers saved:\n" + str(new_question_list))
    except FileNotFoundError:
        new_question_list = QuestionList()

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using 'Python Learning App'? ")
    while continue_using == "Y":
        allowed_actions: list = ["ADD ANSWER", "REMOVE ANSWER", "ASK QUESTION", "REMOVE QUESTION", "VIEW Q & A"]
        print("Enter 'ADD ANSWER' to add an answer to a question.")
        print("Enter 'REMOVE ANSWER' to remove an answer to a question.")
        print("Enter 'ASK QUESTION' to ask a question.")
        print("Enter 'REMOVE QUESTION' to remove a question.")
        print("Enter 'VIEW Q & A' to view a list of questions and answers.")
        action: str = input("What do you want to do? ")
        while action not in allowed_actions:
            print("Enter 'ADD ANSWER' to add an answer to a question.")
            print("Enter 'REMOVE ANSWER' to remove an answer to a question.")
            print("Enter 'ASK QUESTION' to ask a question.")
            print("Enter 'REMOVE QUESTION' to remove a question.")
            print("Enter 'VIEW Q & A' to view a list of questions and answers.")
            action = input("Sorry, invalid input! What do you want to do? ")

        if action == "ADD ANSWER":
            # Clearing command line window
            clear()

            # Checking whether questions exist or not
            if len(new_question_list.get_questions()) > 0:
                print("Below is a list of questions and answers.\n" + str(new_question_list))

                question_index: int = int(input("Please enter the index of the question you want to answer (1 - " +
                                                str(len(new_question_list.get_questions())) + "): "))
                while question_index < 1 or question_index > len(new_question_list.get_questions()):
                    question_index = int(input("Sorry, invalid input! Please enter the index of the question you want "
                                               "to answer (1 - " + str(len(new_question_list.get_questions())) + "): "))

                to_answer: Question = new_question_list.get_questions()[question_index - 1]
                answer: str = input("Please enter your answer: ")
                to_answer.add_answer(answer)
            else:
                pass
        elif action == "REMOVE ANSWER":
            # Clearing command line window
            clear()

            # Checking whether questions exist or not
            if len(new_question_list.get_questions()) > 0:
                print("Below is a list of questions and answers.\n" + str(new_question_list))

                question_index: int = int(input("Please enter the index of the question you want to remove answer from (1 - " +
                                                str(len(new_question_list.get_questions())) + "): "))
                while question_index < 1 or question_index > len(new_question_list.get_questions()):
                    question_index = int(input("Sorry, invalid input! Please enter the index of the question you want "
                                               "to remove answer from (1 - " + str(len(new_question_list.get_questions())) + "): "))

                to_remove_answer: Question = new_question_list.get_questions()[question_index - 1]
                answer_index: int = int(input("Please enter the index of the answer you want to remove (1 - " +
                                              str(len(to_remove_answer.get_answers())) + "): "))
                while answer_index < 1 or answer_index > len(to_remove_answer.get_answers()):
                    answer_index = int(input("Sorry, invalid input! Please enter the index of the answer you want "
                                             "to remove (1 - " + str(len(to_remove_answer.get_answers())) + "): "))

                answer_to_remove: str = to_remove_answer.get_answers()[answer_index - 1]
                to_remove_answer.remove_answer(answer_to_remove)
            else:
                pass
        elif action == "ASK QUESTION":
            # Clearing command line window
            clear()

            question: str = input("What do you want to ask? ")
            new_question_list.add_question(question)
        elif action == "REMOVE QUESTION":
            # Clearing command line window
            clear()

            # Checking whether questions exist or not
            if len(new_question_list.get_questions()) > 0:
                print("Below is a list of questions and answers.\n" + str(new_question_list))

                question_index: int = int(input("Please enter the index of the question you want to remove (1 - " +
                                                str(len(new_question_list.get_questions())) + "): "))
                while question_index < 1 or question_index > len(new_question_list.get_questions()):
                    question_index = int(input("Sorry, invalid input! Please enter the index of the question you want "
                                               "to remove (1 - " + str(len(new_question_list.get_questions())) + "): "))

                to_be_removed: Question = new_question_list.get_questions()[question_index - 1]
                new_question_list.remove_question(to_be_removed)
            else:
                pass
        elif action == "VIEW Q & A":
            # Clearing command line window
            clear()

            print(new_question_list)
            print("\n")
            input_string: str = input("Enter anything to proceed: ")
        else:
            pass  # Do nothing

        # Clearing command line window
        clear()

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using 'Python Learning App'? ")
    # Automatically saving the question list
    save_question_list(new_question_list, file_name)
    sys.exit()


if __name__ == '__main__':
    main()
