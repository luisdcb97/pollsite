// const json = '[{"text": "Antonio Louro - Lambe Cus", "children": [{"text": "José Teodoro - Teddy", "children": [{"text": "Luís Bernarda - Luizard", "children": []}, {"text": "Alexandra Velosa - Xana", "children": []}, {"text": "Ricardo Paiva", "children": []}]}, {"text": "Vitor Ferreira - Gay", "children": [{"text": "Ana Clara", "children": []}]}, {"text": "Alexandra Nogueira - Alex", "children": []}]}]';

// const arvores = JSON.parse(json);
const arvores = json;

const angel_config = {
    chart: {
        container: "#tree-simple",  // id of the html div element
        node: {
            collapsable: true   // enable collapsing of lower nodes into the ones above
        },
        connectors: {
            type: 'step'
        },
        subTeeSeparation: 75,
        levelSeparation: 75,
        siblingSeparation: 40,
        hideRootNode: true,
    },
    nodeStructure: {
        text: "Big Boss",   // create "phantom" node to act as holder for all disconnected roots
        children: []
    }
};

// let stack = [];
// stack.push(...arvores);
// // node.text é um objeto e não uma string direta
// for (let node of stack){
//     if (node.children.length === 0){
//         node.HTMLclass = "leaf-node";    // adiciona classe para os nos terminais se destacarem
//     }
//     stack.push(...node.children);
// }

for (let root of arvores){
    angel_config.nodeStructure.children.push(root);
}

const my_chart = new Treant(angel_config);