#################################
# Define Variables

name = "Arshia" # str
age = 20        # int
score = 19.5    # float
is_male = True  # bool

#################################
# Convert Variables

int(score)      # 19
int(is_male)    # 1
int(name)       # ValueError

str(age)        # "20"
str(score)      # "19.5"
str(is_male)    # "True"

float(name)     # ValueError
float(age)      # 20.0
float(is_male)  # 1.0

bool(name)      # True
bool(age)       # True
bool(score)     # True
bool("")        # False
bool(0)         # False
