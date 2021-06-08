import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(wood.head())
print(len(wood))
print(steel.head())
print(len(steel))


# write function to plot rankings over time for 1 roller coaster here:
def ranking_over_time_one_coaster(coaster_name, park_name, ranking_df):
    df = ranking_df[(ranking_df.Name == coaster_name)
                    & (ranking_df.Park == park_name)]
    # print(df)
    plt.title("{} Rankings".format(coaster_name))
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.gca().invert_yaxis()
    plt.plot(df['Year of Rank'], df['Rank'])
    plt.show()


ranking_over_time_one_coaster("El Toro", "Six Flags Great Adventure", wood)
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:


def ranking_over_time_two_coasters(coaster_one_name, park_one_name, coaster_two_name, park_two_name, ranking_df):
    df_one = ranking_df[(ranking_df.Name == coaster_one_name)
                        & (ranking_df.Park == park_one_name)]
    df_two = ranking_df[(ranking_df.Name == coaster_two_name)
                        & (ranking_df.Park == park_two_name)]

    # print(df)
    plt.title("{} vs. {} Rankings".format(coaster_one_name, coaster_two_name))
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.gca().invert_yaxis()
    plt.plot(df_one['Year of Rank'], df_one['Rank'], label=coaster_one_name)
    plt.plot(df_two['Year of Rank'], df_two['Rank'], label=coaster_two_name)
    plt.legend()
    plt.show()


ranking_over_time_two_coasters(
    "El Toro", "Six Flags Great Adventure", "Boulder Dash", "Lake Compounce", wood)

plt.clf()

# write function to plot top n rankings over time here:


def top_n_ranked_coasters(n, ranking_df):
    df = ranking_df[ranking_df.Rank <= n]
    # print(df)

    coasters = df.Name.unique()
    plt.title("Top {} Ranked Coasters".format(n))
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.gca().invert_yaxis()

    for coaster in coasters:
        curr_df = df[df.Name == coaster]
        plt.plot(curr_df['Year of Rank'], curr_df['Rank'], label=coaster)

    plt.legend()
    plt.show()


top_n_ranked_coasters(5, wood)
plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')
print(roller_coasters.head())

# write function to plot histogram of column values here:


def plot_hist(df, col_name):

    plt.hist(df[col_name])
    plt.title("Histogram of roller coaster {}".format(col_name))
    plt.xlabel(col_name)
    plt.ylabel("count")
    plt.show()


plot_hist(roller_coasters, 'speed')
plt.clf()

# write function to plot inversions by coaster at a park here:


def plot_inversions_bar(df, park_name):
    plt.bar(df.name[df.park == park_name],
            df.num_inversions[df.park == park_name])
    plt.xticks(rotation=90)
    plt.title("Num of inversions for each coaster in {}".format(park_name))
    plt.xlabel("coaster name")
    plt.ylabel("num of inversions")
    plt.show()


plot_inversions_bar(roller_coasters, "Six Flags Great Adventure")
plt.clf()

# write function to plot pie chart of operating status here:


def plot_pie_op_status(df):
    num_operating = len(df[df.status == 'status.operating'])
    num_closed = len(df[df.status == 'status.closed.definitely'])
    print(num_operating)
    print(num_closed)

    plt.pie([num_operating, num_closed], autopct='%0.1f%%',
            labels=['Operating', 'Closed'])
    plt.title("Roller coaster operating status")
    plt.show()


plot_pie_op_status(roller_coasters)
plt.clf()

# write function to create scatter plot of any two numeric columns here:


def plot_scatter(df, col_one, col_two):
    plt.scatter(df[col_one], df[col_two])
    plt.title("{} vs. {}".format(col_one, col_two))
    plt.xlabel(col_one)
    plt.ylabel(col_two)
    plt.show()


# plot_scatter(roller_coasters, 'speed', 'height')
# remove height outliers
plot_scatter(roller_coasters[roller_coasters.height < 140], 'speed', 'height')
plt.clf()
