import matplotlib.pyplot as plt

def test_graphs(): 
    name = "Test station"
    dates=["2012","2013","2014"]
    levels=[1.01,1.04,1.02]
    dates = []
    levels = []
    plt.plot(dates, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date (days)')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    plt.title(name)
    #plt.show()
    #plt.tight_layout()

    #assert plt.plot.called

