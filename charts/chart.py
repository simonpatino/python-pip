import matplotlib.pyplot as plt

def generate_piechart():
    labels=["A","B","C"]
    values= [200,34,129]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()

     
