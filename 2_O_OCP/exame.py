from abc import abstractclassmethod, ABC

class ExamesInterface(ABC):

    @abstractclassmethod
    def verifica_condicoes():
        pass

    @abstractclassmethod
    def aprova_condicoes():
        pass


class ExameSangue(ExamesInterface):

    def aprova_condicoes():
        if True:
            print("Aprova condições")

    def verifica_condicoes():
        print("Validando Exame de Sangue")

class ExameRaioX(ExamesInterface):

    def aprova_condicoes():
        if True:
            print("Aprova condições")

    def verifica_condicoes():
        print("Validando Exame de Raio-X")

exame_sangue = ExameSangue()
exame_raiox = ExameRaioX()