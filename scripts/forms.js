$(document).ready(function() {


    console.log("Working");

    var nodes = new vis.DataSet([
        {id: 1, label: 'Node 1'},
        {id: 2, label: 'Node 2'},
        {id: 3, label: 'Node 3'},
        {id: 4, label: 'Node 4'},
        {id: 5, label: 'Node 5'},
        {id: 6, label: 'Node 6'},
        {id: 7, label: 'Node 7'},
        {id: 8, label: 'Node 8'},
    ]);
    // create an array with edges
    var edges = new vis.DataSet([
        {from: 1, to: 2},
        {from: 2, to: 3},
        {from: 3, to: 4},
        {from: 4, to: 5},
        {from: 5, to: 6},
        {from: 6, to: 7},
        {from: 7, to: 8},
    ]);



    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};

    // initialize your network!
    var network = new vis.Network(container, data, options);
    console.log("Editing Network");

    jQuery('body').hover(function() {
      //$('').clone({left:'0px'}, 1500, 'easeInElastic', function() {
      // console.log("Adding node");
      // nodes.push({id: 12, label : 'Node Test'})
      // console.log(String(nodes));
        var add = {
          manipulation: {
            addNode: function(nodeData,callback) {
              nodeData.label = 'Create a new node';
              callback(nodeData);
            }
          }
        }
        //getNodes.push({id : 12, label : "Test Node"})
        //edges.push({from: 8, to: 12})
        console.log("Creating a node 2");

        container = document.getElementById('mynetwork');

        // provide the data in the vis format
        data = {
            nodes: nodes,
            edges: edges
        };
        network.container = container;
        network.data = data;
        network.options = add;

      });

      function getNodes() {
        return nodes;
      }

})
// });
