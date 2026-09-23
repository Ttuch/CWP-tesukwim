import sys

def downcase_all(lst):
    for i in range(1, len(lst), 1):
        print(lst[i].lower())

num_para = len(sys.argv) - 1

if num_para >= 1:
    downcase_all(sys.argv)
else :
    print("none")