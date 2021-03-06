#!/Users/jacogericke/anaconda3/bin/python3

import time
import math
from copy import deepcopy

INPUT1 = ["R994","D213","L483","U102","L292","U153","L123","D568","R54","U482","L971","D679","L17","U492","R448","U75","R472","D209","R872","D271","L271","U175","L373","D968","R867","U191","R746","U717","L918","D171","L205","D399","R889","D626","R683","D853","R571","U42","L406","D390","R716","U364","L596","U226","L34","D805","R474","D304","R54","D854","L140","U923","L800","D833","L127","D576","R779","U433","L270","U602","L266","D874","R275","D146","L469","U623","R932","D564","R683","D769","L824","U818","L743","U846","R607","D860","R989","U927","R467","D465","R915","D531","L206","U366","R476","U516","R688","D144","L3","D612","L50","D519","R765","D684","L100","U233","R898","U957","R335","D614","R672","U428","R104","U294","L817","D83","R165","U328","L348","D231","R192","D982","R930","D949","R849","D144","R181","D691","R953","D796","L262","D883","L141","U264","L876","U445","R705","U802","L418","U177","R695","U138","L486","D598","R473","D704","R322","U818","R740","U218","R718","D942","R621","D277","L277","U338","L134","U586","L32","U89","L117","U296","R954","D775","L744","D655","R405","U67","R586","U37","L976","D486","L431","U671","R871","D865","R671","D434","L754","D933","L353","D430","L494","D729","R88","D438","R301","D111","L70","U561","L446","D973","R646","D419","R499","D496","L933","D463","L624","U999","L899","U954","R971","U533","R110","U483","R100","D452","R143","D73","L144","D220","L621","U62","R695","U270","L655","U404","L207","U946","L989","U767","L953","U271","L206","U315","L675","D579","L910","D413","R283","D118","L405","U724","L144","U969","R256","D940","L592","D714","L898","D937","R3","D175","L578","D981","R110","D217","L60","D57","R559","D913","R251","D883","L431","U450","L755","D126","L236","U532","R62","U33","L499","D29","R304","U25","R923","U732","L930","U812","R923","D12","L991","U223","R58","D638","R166","D980","R999","D825","L707","D956","L107","U676","R263","U949","L924","D928","L747","U641","L179","D398","R714","U715","R525","D515","R887","D21","R100","D424","L265","U704","R119","U77","L619","D308","R857","U272","L571","U650","L793"]
INPUT2 = ["L1010","D906","R561","D862","R541","D243","L958","D538","L930","U270","R282","D56","R692","U625","R962","U95","L834","D477","R375","D859","L158","D664","L874","U817","R218","U428","L194","U713","R1","D291","R608","D79","L582","U570","R952","U217","R441","U43","L966","U40","R103","U419","L387","U198","R306","U239","R714","U193","L111","D98","L308","U856","L702","D596","R903","D607","R86","D967","L191","D676","R606","D638","R512","D373","L623","U596","L151","U394","L241","D429","L324","D710","L663","U821","L351","D538","L917","U449","R120","D746","R833","U812","L691","D751","L631","U612","L107","D276","L997","D764","R644","U823","L574","U276","L48","U968","L97","D118","L976","U511","L976","U862","L232","D425","R586","U665","R893","D744","R317","D152","L406","U997","R377","D552","R226","D960","L232","D834","L911","U548","L127","U845","L687","U835","R18","D524","R226","D896","R89","U497","L748","U105","R174","U17","R212","U347","L942","U633","R799","U907","L971","D490","R690","D399","L725","U807","R244","U558","L754","D490","L726","D126","L639","D548","L18","D173","L188","D33","L707","D980","L728","U663","R593","D172","R314","U873","R409","U476","R312","U970","R28","U514","L378","D681","R611","U733","R135","U682","L736","D253","L432","D736","L777","U447","L174","D664","L652","D984","L714","D990","R608","D383","R51","U497","L343","D569","R515","D144","L949","D827","R112","U595","L109","D215","L401","U635","L953","U20","R780","U324","R955","D346","R762","D693","R56","U341","R481","U70","R385","U330","R278","D923","L835","D733","R235","U628","R505","U372","R469","D659","R618","U899","L21","U698","R688","U409","R775","D405","R846","D783","R675","U261","R721","D637","R957","D355","L50","U759","R769","D612","R538","U923","L780","U786","R104","D66","L67","U175","L820","D723","R124","U937","R923","D130","R758","U678","R215","U671","R366","U163","L783","U790","L832","D731","L736","D879","R508","U433","R705","U939","L969","U920","R683","D188","L349","U812","L36","D333","L88","U356","L140","D735","L217","D365","R23","D88","L20","D854","L437","U153","L307"]


class Path(object):

    def __init__(self, directions=[]):
        self.directions = directions
        self.grid = []
        self.steps = 0
        self.X = 0
        self.Y = 0

    def calculate(self):

        for i in self.directions:
            
            if i.startswith('D'):
                self.update_grid( int(i.strip('D')), down_not_up=1)
            elif i.startswith('U'):
                self.update_grid( int(i.strip('U')), down_not_up=-1)
            elif i.startswith('R'):
                self.update_grid( int(i.strip('R')), right_not_left=1)
            elif i.startswith('L'):
                self.update_grid( int(i.strip('L')), right_not_left=-1)

        return self.grid

    def update_grid(self, value, down_not_up=0, right_not_left=0):
        path_obj = {'dir': 'X' if down_not_up == 0 else 'Y',
                    'x_start': self.X if right_not_left != -1 else self.X + (value * right_not_left),
                    'y_start': self.Y if down_not_up != -1 else self.Y + (value * down_not_up),
                    'x_end': self.X if right_not_left == -1 else self.X + (value * right_not_left),
                    'y_end': self.Y if down_not_up == -1 else self.Y + (value * down_not_up),
                    'steps': self.steps}

        self.grid.append(path_obj)

        self.X += value * right_not_left
        self.Y += value * down_not_up
        self.steps += value
        

    @classmethod
    def get_distance(cls, grid1, grid2):
        min_steps = None
        for path1 in grid1:
            for path2 in grid2:
                tmp = cls.compare_paths(path1, path2)
                if tmp != None:
                    if min_steps == None:
                        min_steps = tmp
                    elif tmp < min_steps:
                        min_steps = tmp
        print("MIN", min_steps)

    @classmethod
    def compare_paths(cls, pth1, pth2):
        if pth1['dir'] == pth2['dir']:
            return None
        else:
            P1 = pth1 if pth1['dir'] == 'X' else pth2
            P2 = pth1 if pth1['dir'] == 'Y' else pth2
        
        if P1['x_start'] < P2['x_start'] and P1['x_end'] > P2['x_start']:
            if P2['y_start'] < P1['y_start'] and P2['y_end'] > P1['y_start']:
                
                P1_steps = P1['steps'] + ( P2['x_start'] - P1['x_start'] )
                P2_steps = P2['steps'] + ( P1['y_start'] - P2['y_start'] )

                print(f"Intersection at {P2['x_start']}, {P1['y_start']} with steps {P1_steps}, {P2_steps}")
                return P1_steps + P2_steps

        return None
            


def test():
    one = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    two = ["U62","R66","U55","R34","D71","R55","D58","R83"]

    ONE = Path(one).calculate()
    TWO = Path(two).calculate()

    Path().get_distance(ONE, TWO)

    one = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
    two = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

    ONE = Path(one).calculate()
    TWO = Path(two).calculate()

    Path().get_distance(ONE, TWO)

def real():
    ONE = Path(INPUT1).calculate()
    TWO = Path(INPUT2).calculate()

    Path().get_distance(ONE, TWO)


if __name__ == "__main__":
    save = time.time()
    real()
    #test()

    print(int(time.time() - save))

