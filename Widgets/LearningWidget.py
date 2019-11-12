from PyQt5.QtWidgets import QWidget
from UI.LearningWidgetUI import Ui_Form
from PyQt5.QtCore import pyqtSignal
import random


class LearnWidget(QWidget, Ui_Form):
    
    finish = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.par = parent

        self.choice = ("a i u e o ka ki ku ke ko sa si su " +
                      "se so ta ti tu te to na ni nu ne no ha hi hu he ho ma " +
                      "mi mu me mo ya yu yo ra ri ru re ro wa wi we wo n").split()
        
        self.katakana = " ".join("アイウエオカキクケコサシスセソタチ)ツテトナ"+
                        "ニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲン").split()
        self.hiragana = " ".join("あいうえおかきくけこさしすせそたちつてとなに"+
                        "ぬねのはひふへほまみむめもやゆよらりるれろわゐゑをん").split()
        self.alphabet = []
        with open("Widgets/alphabet.txt", "r") as file:
            alph = file.read().strip(" \n\t")
            if alph == "k":
                self.alphabet = self.katakana
            else:
                self.alphabet = self.hiragana
        
        self.answers = [self.answer_1, self.answer_2, self.answer_3]
        self.nextBtn.setVisible(False)
        self.scoring.setText("Score: 0")
        self.nextBtn.clicked.connect(self.next)
        self.set_question()
        self.submitBtn.clicked.connect(self.submit)
        self.finishBtn.clicked.connect(self.save_score)
        

    def set_question(self):
        random_ind = random.randrange(len(self.alphabet) - 1)
        self.questionLabel.setText(self.alphabet[random_ind])
        self.right_answer = self.choice[random_ind]
        tmp_choicies = self.choice[:]
        tmp_choicies.remove(self.right_answer)
        already = []
        for answer in self.answers:
            random_ind = random.randrange(len(tmp_choicies))
            if random_ind not in already:
                already.append(random_ind)
            else:
                pass
            answer.setText(tmp_choicies[random_ind])
        ind = random.randrange(3)
        self.answers[ind].setText(self.right_answer)


    def submit(self):
        for answer in self.answers:
            if answer.isChecked():
                if answer.text() == self.right_answer:
                    self.questionLabel.setText("Right !")
                    score = int(self.scoring.text().split()[1]) + 1
                    self.scoring.setText(f"Score: {score}")
                else:
                    self.questionLabel.setText("Wrong !")
                self.nextBtn.setVisible(True)
                self.submitBtn.setVisible(False)
                answer.setCheckable(False)
            answer.setCheckable(False)

    
    def next(self):
        self.submitBtn.setVisible(True)
        self.nextBtn.setVisible(False)
        for answer in self.answers:
            answer.setChecked(False)
            answer.setCheckable(True)

        self.set_question()


    def save_score(self):
        with open("Widgets/score.txt", "w") as file:
                file.write(self.scoring.text().split()[1])
                file.close()
        self.finish.emit()
        
    def reload(self):
        with open("Widgets/alphabet.txt", "r") as file:
            alph = file.read().strip(" \n\t")
            if alph == "k":
                self.alphabet = self.katakana
            else:
                self.alphabet = self.hiragana
        self.scoring.setText("Score: 0")
        self.set_question()