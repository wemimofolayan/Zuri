class Student:

    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score =  float(score)
      
    def change_name(self, n_name):
        self.n_name = n_name
        n_name = "Peter"
        print(f'the student updated name from {self.name} to {n_name}' )
    
    def change_age(self, n_age):
        self.n_age = n_age
        n_age = 34
        print(f'the student updated Age from {self.age} to {n_age}' )
    
    
    def add_track(self, add_tracks):
        self.add_tracks = add_tracks
        add_tracks = "UI/UX"
        print(f'the student added new track:', add_tracks)
    
    def get_score(self, n_score):
        self.n_score = n_score
        n_score =10.90
        return(f'the student updated score is',n_score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

print(Bob.name)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(10.90)

