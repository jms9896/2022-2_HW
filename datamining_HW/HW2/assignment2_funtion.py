import sys

def main(args):
    with open(args, 'r', encoding='UTF-8') as file:
        genes_full = file.read().split()
        genes_slice = []
        for i in range(len(genes_full)%12):
            for j in range(len(genes_full)):
                genes_slice[i].append(genes_full[j])
        # print(genes)


if __name__ == '__main__':
    main(sys.argv[1])