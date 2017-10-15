import math
def score():
    try:
        s = math.floor(float(input("Enter Score: "))*10)/10
        print(s)
        d = {1.0: 'A', 0.9: 'A', 0.8: 'B', 0.7: 'C', 0.6: 'D', 0.5: 'F', 0.4: 'F', 0.3: 'F', 0.2: 'F', 0.1: 'F', 0.0: 'F' }
        if s >= 0.0 and s <= 1.0:
            print(d[s])
        else:
            print('Bad score')
            return score()
    except Exception as e:
        print('Bad score')
        return score()
if __name__ == '__main__':
    score()