document.addEventListener('DOMContentLoaded', function() {

const nodes = [
    { id: "TX", type: "TX" },
    { id: "RX1", type: "RX" },
    { id: "RX2", type: "RX" },
    { id: "RX3", type: "RX" },
    { id: "RX4", type: "RX" },
    ...Array.from({length: 16}, (_, i) => ({ id: `PoE${i+1}`, type: "PoE" }))
];

// Initialize node positions in a circle
const centerX = 450, centerY = 450, radius = 300;
const total = nodes.length;
nodes.forEach((node, i) => {
    if (node.id === "TX") {
        node.x = centerX;
        node.y = centerY;
    } else {
        const angle = 2 * Math.PI * (i-1) / (total-1);
        node.x = centerX + radius * Math.cos(angle);
        node.y = centerY + radius * Math.sin(angle);
    }
});

const links = [
    { source: "TX", target: "RX1", type: "fiber" },
    { source: "TX", target: "RX2", type: "fiber" },
    { source: "TX", target: "RX3", type: "fiber" },
    { source: "TX", target: "RX4", type: "fiber" },
    { source: "TX", target: "RX1", type: "power" },
    { source: "TX", target: "RX2", type: "power" },
    { source: "TX", target: "RX3", type: "power" },
    { source: "TX", target: "RX4", type: "power" },
    { source: "RX1", target: "PoE1", type: "data" },
    { source: "RX1", target: "PoE2", type: "data" },
    { source: "RX2", target: "PoE3", type: "data" },
    { source: "RX2", target: "PoE4", type: "data" },
    { source: "RX2", target: "PoE5", type: "data" },
    { source: "RX3", target: "PoE6", type: "data" },
    { source: "RX3", target: "PoE7", type: "data" },
    { source: "RX4", target: "PoE8", type: "data" },
    { source: "RX4", target: "PoE9", type: "data" },
    { source: "RX4", target: "PoE10", type: "data" },
    { source: "RX1", target: "PoE11", type: "data" },
    { source: "RX2", target: "PoE12", type: "data" },
    { source: "RX3", target: "PoE13", type: "data" },
    { source: "RX3", target: "PoE14", type: "data" },
    { source: "RX4", target: "PoE15", type: "data" },
    { source: "RX4", target: "PoE16", type: "data" }
];

const svg = d3.select("svg");
const width = +svg.attr("width");
const height = +svg.attr("height");

const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links)
        .id(d => d.id)
        .distance(100))
    .force("charge", d3.forceManyBody().strength(-500))
    .force("center", d3.forceCenter(width / 2, height / 2));

// Count duplicates and assign curve indices
const linkPairs = {};
links.forEach(d => {
    const key = `${d.source}-${d.target}`;
    if (!linkPairs[key]) linkPairs[key] = [];
    linkPairs[key].push(d);
});

links.forEach(d => {
    const key = `${d.source}-${d.target}`;
    const group = linkPairs[key];
    d.pairIndex = group.indexOf(d);
    d.pairCount = group.length;
});

const linkGroup = svg.append("g").attr("class", "links");
const link = linkGroup.selectAll("path")
    .data(links)
    .enter()
    .append("path")
    .attr("class", d => `link ${d.type}`)
    .attr("fill", "none")
    .attr("stroke-width", 2);


const nodeGroup = svg.append("g").attr("class", "nodes");
const nodeSel = nodeGroup.selectAll("g")
    .data(nodes)
    .enter()
    .append("g")
    .attr("class", "node")
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

nodeSel.append("circle")
    .attr("r", 25)
    .attr("fill", "#c9a3e8")
    .attr("stroke", "#7b2cbf")
    .attr("stroke-width", 2);

nodeSel.append("text")
    .text(d => d.id)
    .attr("text-anchor", "middle")
    .attr("dy", ".3em")
    .attr("font-size", "11px")
    .attr("font-weight", "bold");

function drawPath(d) {
    // Safety checks
    if (!d.source || !d.target) return '';
    if (typeof d.source.x !== 'number' || typeof d.source.y !== 'number' ||
        typeof d.target.x !== 'number' || typeof d.target.y !== 'number') {
        return '';
    }
    if (isNaN(d.source.x) || isNaN(d.source.y) || isNaN(d.target.x) || isNaN(d.target.y)) {
        return '';
    }
    
    const offset = (d.pairIndex - (d.pairCount - 1) / 2) * 20;
    const dx = d.target.x - d.source.x;
    const dy = d.target.y - d.source.y;
    const len = Math.sqrt(dx * dx + dy * dy) || 1;
    const mx = (d.source.x + d.target.x) / 2 - dy / len * offset;
    const my = (d.source.y + d.target.y) / 2 + dx / len * offset;
    return `M${d.source.x},${d.source.y}Q${mx},${my}${d.target.x},${d.target.y}`;
}

simulation.on("tick", () => {
    link.attr("d", drawPath);
    nodeSel.attr("transform", d => `translate(${d.x},${d.y})`);
});

// Don't force restart - let simulation proceed naturally
// setTimeout(() => {
//     simulation.alpha(1).restart();
// }, 0);

// Drag functions
function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

}); // End DOMContentLoaded
