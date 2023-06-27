
import pandas as pd
import numpy as np
import igraph as ig
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from chart_studio import plotly as py
from plotly.graph_objs import *
from plotly.offline import iplot
from py2neo import Graph

def plot_community(session, query: str, community: str):
    """Function to plot the network and color the nodes based on the community

    Args:
        query (str): the query to fiter out the nodes and edges to plot
        community (str): the community to color the nodes

    Returns:
        fig: plot of the network
    """

    edges = list()
    edge_w = list()
    vertices = dict()

    results = session.run(query)

    g = ig.Graph()

    for result in results:
        vertices[str(result["n"]["label"])] = str(result["n"][community])
        vertices[str(result["m"]["label"])] = str(result["m"][community])
        edges.append([str(result["n"]["label"]), str(result["m"]["label"])])
        edge_w.append(1/result["r"]["weight"])

    g.add_vertices(list(vertices.keys()))
    g.add_edges(edges)
    g.es["weight"] = edge_w
    g.vs["community"] = list(vertices.values())
    N = len(g.vs)
    E = [e.tuple for e in g.es]

    jon_id = g.vs.find(name="Jon").index


    arya_id = g.vs.find(name="Arya").index
    sansa_id = g.vs.find(name="Sansa").index
    bran_id = g.vs.find(name="Bran").index

    tyrion_id = g.vs.find(name="Tyrion").index
    cersei_id = g.vs.find(name="Cersei").index
    jaime_id = g.vs.find(name="Jaime").index

    daenerys_id = g.vs.find(name="Daenerys").index
    stannis_id = g.vs.find(name="Stannis").index

    community_list = list(set(list(vertices.values())))

    k = len(community_list)

    colors = px.colors.qualitative.Plotly[:k]

    g.vs['color'] = [None]

    color_list = list()

    for i in list(vertices.values()):
        color_id = community_list.index(i)
        color_list.append(colors[color_id])

    g.vs['color'] = color_list

    layt = g.layout("fr")

    Xn = [layt[k][0] for k in range(N)]

    Yn = [layt[k][1] for k in range(N)]
    Xe = []
    Ye = []

    for e in E:
        Xe += [layt[e[0]][0], layt[e[1]][0], None]
        Ye += [layt[e[0]][1], layt[e[1]][1], None]

    fig = go.Figure()

    trace1 = go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        )
    trace2 = go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='ntw',
                        marker=dict(symbol='circle-dot',
                                    size=10,
                                    color=g.vs["color"],
                                    line=dict(color='rgb(50,50,50)', width=0.5)
                                    ),
                        text=g.vs["name"],
                        hoverinfo='text'
                        )

    fig.add_trace(trace1)
    fig.add_trace(trace2)

    fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False)

    # axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
    #             zeroline=False,
    #             showgrid=False,
    #             showticklabels=False,
    #             title=''
    #             )

    fig.update_layout(title="Game of Thrones Networks for ",
                      font=dict(size=12),
                      showlegend=False,
                      autosize=False,
                      width=800,
                      height=800,
                      margin=layout.Margin(
                          l=40,
                          r=40,
                          b=85,
                          t=100,
                      ),
                      hovermode='closest',
                      # annotations=[
                      #     dict(
                      #         showarrow=False,
                      #         text='This igraph.Graph has the Kamada-Kawai layout',
                      #         xref='paper',
                      #         yref='paper',
                      #         x=0,
                      #         y=-0.1,
                      #         xanchor='left',
                      #         yanchor='bottom',
                      #         font=dict(
                      #             size=14
                      #         )
                      #     )
                      # ]
                      )

    # data = [trace1, trace2]
    # fig = Figure(data=data, layout=layout)
    # py.iplot(fig, filename='Coautorship-network-igraph')

    fig.add_annotation(
        x=Xn[jon_id],
        y=Yn[jon_id],
        xref="x",
        yref="y",
        text="Jon Snow",

    )


    fig.add_annotation(
        x=Xn[arya_id],
        y=Yn[arya_id],
        xref="x",
        yref="y",
        text="Arya Stark",
    )

    fig.add_annotation(
        x=Xn[sansa_id],
        y=Yn[sansa_id],
        xref="x",
        yref="y",
        text="Sansa Stark",
    )

    fig.add_annotation(
        x=Xn[bran_id],
        y=Yn[bran_id],
        xref="x",
        yref="y",
        text="Bran Stark",
    )

    fig.add_annotation(
        x=Xn[tyrion_id],
        y=Yn[tyrion_id],
        xref="x",
        yref="y",
        text="Tyrion Lannister",
    )

    fig.add_annotation(
        x=Xn[cersei_id],
        y=Yn[cersei_id],
        xref="x",
        yref="y",
        text="Cersei Lannister",
    )

    fig.add_annotation(
        x=Xn[jaime_id],
        y=Yn[jaime_id],
        xref="x",
        yref="y",
        text="Jaime Lannister",
    )

    fig.add_annotation(
        x=Xn[daenerys_id],
        y=Yn[daenerys_id],
        xref="x",
        yref="y",
        text="Daenerys Targaryen",
    )

    fig.add_annotation(
        x=Xn[stannis_id],
        y=Yn[stannis_id],
        xref="x",
        yref="y",
        text="Stannis Baratheon",
    )

    return fig
