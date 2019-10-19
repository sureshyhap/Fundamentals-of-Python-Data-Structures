class Student():
    def __init__(self, name, num_scores):
        self.name = name
        self.scores = []
        for i in range(num_scores):
            self.scores.append(0)

    def access(self, position):
        return self.scores[position]

    def replace(self, position, new_score):
        self.scores[position] = new_score

    def get_number(self):
        return len(self.scores)

    def get_highest(self):
        return max(self.scores)

    def get_averageg(self):
        return sum(self.scores) / len(self.scores)

    def get_name(self):
        return self.name

    def __str__(self):
        s = "Name: " + self.name + "\n"
        count = 1
        for score in self.scores:
            s += "Score " + str(count) + ": " + str(score) + "\n"
        return s

def main():
    joseph = Student("Suresh Yhap", 3)
    joseph.replace(0, 88)
    joseph.replace(1, 77)
    joseph.replace(2, 100)
    print(joseph)

if __name__ == "__main__":
    main()

    
