'''
Agent-based model on evolution of cooperation and defection in a biological network without costly punishment. Tests the impact of diversity and decreasing density of connectivity on cooperation.
'''
import networkx as nx
import matplotlib.pyplot as plt
from random import *
import pandas as pd
from collections import Counter
import pdb #; pdb.set_trace()

strategy = [] #list of strategies
stat = 1 #counter for games
limit = 1e+2 #limit for counter above ("stat") which is also number of games to be played
avg_payoff = 0 #average payoff
c_1 = 0 #number of games where players cooperated more than defected
d_1 = 0 #number of games where players defected more than cooperated
while stat <= limit:
 
    Network = {} #dictionary of networks
    total_num = 36
    defect = sample(range(1, total_num + 1), int(total_num/2))
    players = [] #nodes
    for i in range(total_num):
        if (i + 1) in defect:
            M = 'D'
        else:
            M = 'C'
        players.append(i)
        Network[i] = [str(i + 1), M, 0, 'N', 0, 0, 0]#[label of node, current strategy, payoff, imitated strategy, payoff for comparison] 

    path = []
    f = 2.0 #multiplying factor
    for gg in range(int(round(total_num * f))):
        x, y = sample(players, 2)
        while ((x, y) in path or (y, x) in path):
            x, y = sample(players, 2)
        path.append((x, y))       

    def random_layering(): #function for diversity of players and connections
        path = []
        for g in range(int(round(total_num * f))):
            x, y = sample(players, 2)
            while ((x, y) in path or (y, x) in path):
                x, y = sample(players, 2)
            path.append((x, y))
        return path
    '''
    def random_layering():
        path = []
        for gl in range(len(players) - 1):
            for um in range(gl + 1, len(players)):
                path.append((players[gl], players[um]))                           
        return path
    '''

    def plotter():
        global labels
        labels = {}
        for j in range(len(Network)):
            labels[j] = Network[j][1]
        pos = nx.spring_layout(G)
        colors = []
        for n in players:
            if n in plot_defect:
                colors.append('r')
            else:
                colors.append('y')
        nx.draw(G, pos, node_color = colors)
        nx.draw_networkx_labels(G, pos,labels, font_size = 14)
        plt.show() #plots the network using Networkx Python Package. Uncommenting these four lines of code makes it possible to visually see and follow how a strategy emerges in the network

    

    def Graph():
        global path, G, labels, Edge
        Connect = False
        while not Connect: #makes sure graph is connected
            G = nx.Graph()   
            G.add_nodes_from(players)
            #path = random_layering() #function that calls for diversity in every round of a game. Commenting this line of code removes diversity in the rounds of the game
            G.add_edges_from(path)
            if nx.is_connected(G): #makes sure graph is a connected graph
                Connect = True
            else:
                path = random_layering() #else, form a new network
        #print("Is graph connected? ", 'Yes' if nx.is_connected(G) else 'No')
        #print("There are", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")
        Edge = G.edges()
        #print("These are the edges we have in the graph: \n", Edge)
        #print("")
        labels = {}
        
        for j in range(len(Network)):
            labels[j] = Network[j][1]
        '''
        pos = nx.spring_layout(G)
        colors = []
        for n in players:
            if n in plot_defect:
                colors.append('r')
            else:
                colors.append('y')
        nx.draw(G, pos, node_color = colors)
        nx.draw_networkx_labels(G, pos,labels, font_size = 14)
        plt.show() #plots the network using Networkx Python Package. Uncommenting these four lines of code makes it possible to visually see and follow how a strategy emerges in the network
        '''

        #payoffs without costly punishment
        '''
        Following Dreber et. al (2008) "Winners don't punish"
        '''


        for k in players: #synchronous update of strategy
            Network[k][4] = Network[k][2]
            for t in G.neighbors(k):
                if Network[t][2] > Network[k][4]:
                    Network[k][4] = Network[t][2]
                    Network[k][3] = Network[t][1]
        for b in players:
            if Network[b][3] != 'N':
                Network[b][1] = Network[b][3]
            

        for s in players:
            #for y in G.neighbors(s):
                #if Network[y][2] > Network[s][2]:
                    #Network[s][3] = Network[y][1]
            
            if Network[s][1] == 'D': #payoff of a defector
                for g in G.neighbors(s):
                    if Network[g][1] == 'C': #when defector meets cooperator
                        Network[s][2] += 4
                    else:                   #payoff of defector and defector
                        Network[s][2] += 0
            else:    #payoff of cooperator
                for h in G.neighbors(s):
                    if Network[h][1] == 'C': #cooperator and cooperator
                        Network[s][2] += 2
                    else:
                        Network[s][2] += -2 #when cooperator meets cooperator
                        
                        

    count = 1 #counter to times of rounds
    times = 1e+3 #number of rounds
    while count <= times:
        #import pdb; pdb.set_trace()
        if count == 1:
            plot_cooperate = []
            plot_defect = []
            for mm in players:
                if Network[mm][1] == 'C':
                    plot_cooperate.append(mm)
                else:
                    plot_defect.append(mm)
        Graph() #calls function to run a round
        plot_cooperate = []
        plot_defect = []
        Same = True
        cooper = 1
        defer = 1
        avg_cooper = 0
        avg_defer = 0
        for kk in range(len(Network)): #counts how much defection and cooperation a player has made in a game
            if Network[kk][1] == 'C':
                plot_cooperate.append(kk)
                Network[kk][-2] += 1
                cooper += 1
                avg_cooper += Network[kk][2]
            else:
                plot_defect.append(kk)
                Network[kk][-1] += 1
                defer += 1
                avg_defer += Network[kk][2]
        #print('avg coop:', avg_cooper/cooper,'avg def:', avg_defer/defer, 'coop:', cooper-1, 'def:', defer-1)
        for z in range(len(Network) - 1):
            if Network[z][1] != Network[z + 1][1]:
                Same = False
                break
        if Same == True:  #case for everyone having the same strategy
            #plotter() #Uncomment this to print graph
            if Network[z][1] == 'D':
                #print('Everyone is a defector\n')
                strategy.append('Defect')
            
            else:
                #print ('Everyone is a cooperator\n')
                strategy.append('Cooperate')
            break
        if count == times and not Same:
            strategy.append('No Preference')
            #print(Network)
            break
        count += 1
    local_payoff = 0
    for pay in range(len(Network)):
        local_payoff += Network[pay][2]
    avg_payoff += local_payoff/total_num
    Coop = 0
    Def = 0
    for mm in Network: #just checks how many players defect more than cooperate or vice versa
        if Network[mm][-2] > Network[mm][-1]:
            Coop += 1
        elif Network[mm][-1] > Network[mm][-2]:
            Def += 1
        else:
            Coop += 1
            Def += 1
    #print(Network)
    if Def > Coop: 
        d_1 += 1
    if Coop > Def:
        c_1 += 1
    #print('\nIt took %s games' %count)
    #print(Network)
    #print('\nIt took %s games' %count)

    stat += 1
#print('Cope:', c_1, ' Defe:', d_1)
coding = Counter(strategy)
if 'Cooperate' not in coding:
    coding['Cooperate'] = 0
if 'No Preference' not in coding:
    coding['No Preference'] = 0
if 'Defect' not in coding:
    coding['Defect'] = 0
avg_payoff = avg_payoff/limit #calculates payoff
print("Average payoff is", avg_payoff)
print("Total agents", total_num)
#coding = {'Defection':strategy.count('Defect'), 'Cooperation':strategy.count('Cooperate'), 'No Preference':strategy.count('No Preference')}

#df = pd.DataFrame(coding, index = range(len(coding)))

df = pd.DataFrame.from_dict(coding, orient= 'index') #creates bar chart of probabilities
df.columns = ['Amount']
df.columns.name = 'Probability'
ax = df.plot(kind='bar')
ax.set_ylabel("Probability of observing strategy")
ax.set_xlabel("Strategy")
ax.set_title('Probability of strategies in biological network')
plt.show() #creates bar chart of probabilities
print(coding)
#print("\n", strategy)
#print("\n", Network)

