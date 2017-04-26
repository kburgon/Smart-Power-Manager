import pypsa

import pandas as pd
import SolarData
import LoadData

from matplotlib import pyplot as plt

# NB: this example will use units of kW and kWh, unlike the PyPSA defaults
# use 24 hour period for consideration
index = pd.date_range("2016-01-01 00:00", "2016-01-03 23:00", freq="H")

# consumption pattern of home applicances
home_usage = pd.Series(LoadData.getTotalLoads()[:72:], index)

# solar PV panel generation per unit of capacity
pv_pu = pd.Series(SolarData.getSolarOutputData(0.15, 1.9)[:72:], index)

# pv_p_nom = 1651.2015 / 1000
pv_p_nom = 5000 / 1000

# availability of charging - i.e. only when parked at office
home_usage_figure = home_usage.plot().figure
home_usage_figure.suptitle('Power Consumption of Home', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('KW', fontsize=16)
home_usage_figure.savefig('home_usage.png')
home_usage_figure.show()
# pv_pu.plot().figure.show()

network = pypsa.Network()

network.set_snapshots(index)

network.add("Bus",
            "home",
            carrier="AC")

network.add("Bus",
            "renewable",
            carrier="AC")

network.add("Bus",
            "grid",
            carrier="AC")

network.add("Bus",
            "battery",
            carrier="Li-ion")

network.add("Load",
            "home loads",
            bus="home",
            p_set=home_usage)

network.add("Generator",
            "PV panel",
            bus="renewable",
            p_nom=pv_p_nom,
            p_max_pu=pv_pu,
            marginal_cost=0)

network.add("Generator",
            "grid",
            bus="grid",
            marginal_cost=0.12,
            p_nom=100000)

network.add("Store",
            "battery storage",
            bus="battery",
            e_cyclic=True,
            e_nom=1.)

network.add("Link",
            "grid to home",
            bus0="grid",
            bus1="home",
            p_nom=100000)

# network.add("Link",
#             "renewable to home",
#             bus0="renewable",
#             bus1="home",
#             p_nom=100000)

network.add("Link",
            "battery to home",
            bus0="battery",
            bus1="home",
            p_nom=100000)

network.add("Link",
            "renewable to battery",
            bus0="renewable",
            bus1="battery",
            p_nom=100000)


network.lopf(network.snapshots)
print("Objective:", network.objective)
with open('objective.txt', 'w') as f:
    f.write('Objective: Total energy used cost: ${}'.format(network.objective))

generator_output = network.generators_t.p.plot().figure
generator_output.suptitle('Generator Output/Power Draw', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('KW', fontsize=16)
generator_output.savefig('generator_output.png')
generator_output.show()
# print("Panel size [kW]:", network.generators.p_nom_opt["PV panel"])

battery_figure = pd.DataFrame(
    {attr: network.stores_t[attr][
        "battery storage"] for attr in ["p", "e"]}).plot(grid=True).figure
battery_figure.suptitle('Battery Status', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('KW / KWh', fontsize=16)
battery_figure.savefig('battery_figure.png')
battery_figure.show()

# print("Losses [kWh/d]:", network.generators_t.p.loc[
#     :, "PV panel"].sum() - network.loads_t.p.loc[:, "driving"].sum())
network_links_figure = network.links_t.p0.plot().figure
network_links_figure.suptitle('Power Through Links', fontsize=20)
plt.xlabel('Time', fontsize=18)
plt.ylabel('KW', fontsize=16)
network_links_figure.savefig('network_links.png')
network_links_figure.show()
