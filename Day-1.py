# Write a function  that
#takes any number of numerical arguments and returns their sum.
#accepts any number of string arguments and returns the longest string.
#takes any number of string arguments and joins them with a hyphen.
#accepts any number of keyword arguments and prints them in the format: key: value
#takes default profile details as a dictionary, then uses **kwargs to update any given fields.


def addition(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum

print(addition(1,2,3,4,5,5))


def longest_string(*strings):
    lengths = []
    for i in strings:
        lengths.append(len(i))
    x = lengths.index(max(lengths))
    return strings[x]

print(longest_string("a","ab","abc","abcd"))

#smart way to do this:
#def longest_string(*strings):
#    return max(strings, key=len)

def join_hypen(*words):
    j = 1
    final_str = []

    for i in words:
        if j < len(words):
            median_str = i + "-"
            final_str.append(median_str)
        else:
            final_str.append(i)
        j += 1

    x = "".join(final_str)
    return x

print(join_hypen("affan", "shaikh", "is", "20", "years", "old"))


def print_kwargs(**students):
    for key,value in students.items():
        print(f"{key}:{value}")

print_kwargs(affan=6,ankon=14,anjali=12)



default_details={"Name":"","Age":0}

def profile_update(**actual_details):
    for key,value in actual_details.items():
        default_details[key]=value
    print(default_details)

profile_update(Name="Affan",Age=45)

