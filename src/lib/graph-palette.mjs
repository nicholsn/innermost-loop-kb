const styles = {
 AISystem:['#386cb0','hexagon'], Benchmark:['#b8860b','star'], Development:['#a0527d','round-rectangle'],
 Facility:['#3b7d57','rectangle'], Hardware:['#76549c','diamond'], Issue:['#97652e','barrel'],
 Organization:['#266b96','rectangle'], Person:['#ad5930','ellipse'], Role:['#537344','triangle'], Theme:['#84603c','octagon'],
};
export function typeStyle(type) {
 if(styles[type]) return {color:styles[type][0],shape:styles[type][1]};
 let hash=0;for(const char of type)hash=(Math.imul(hash,31)+char.charCodeAt(0))>>>0;
 return {color:`hsl(${hash%360}, 45%, 40%)`,shape:['ellipse','diamond','hexagon','triangle'][hash%4]};
}
