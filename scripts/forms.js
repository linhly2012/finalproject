$(document).ready(function() {


    // var x = document.getElementById("mynetwork").value;
    // console.log(x);

    console.log("Working");

    var nodes = new vis.DataSet([
        {id: 1, label: "name"},
        {id: 2, label: "name2"}
    ]);

    console.log(nodes);
    // create an array with edges
    var edges = new vis.DataSet([
        {from: 1, to: 2}
    ]);


    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };

    //CSS properties of the nodes
    var options = {
      nodes: {
        borderWidth: 5,
        shape: 'circle'
      },
    };

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


})
// });
