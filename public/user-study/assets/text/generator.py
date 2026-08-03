from pygments import highlight
from pygments.lexers import JavascriptLexer, JsonLexer
from pygments.formatters import HtmlFormatter

d3_code = """lineChart = {
  const width = 400;
  const height = 300;
  const marginTop = 20;
  const marginRight = 30;
  const marginBottom = 40;
  const marginLeft = 50;

  const x = d3.scaleLinear(
    d3.extent(carsYearly, d => d.Year), 
    [marginLeft, width -marginRight]
  );

  const y = d3.scaleLinear(
    [0, 35], 
    [height - marginBottom, marginTop]
  );

  const line = d3.line()
      .x(d => x(d.Year))
      .y(d => y(d.Average_MPG));

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height)
      .attr("viewBox", [0, 0, width, height])
      .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

  svg.append("g")
  .attr("transform", `translate(0,${height - marginBottom})`)
  .call(
    d3.axisBottom(x)
      .tickValues(d3.range(1970, 1983, 2))
      .tickFormat(d3.format("d"))
  )
  .call(g => g.append("text")
      .attr("x", width / 2 + 10)
      .attr("y", marginBottom - 10)
      .attr("fill", "currentColor")
      .attr("text-anchor", "middle")
      .text("Year")
  );

  svg.append("g")
      .attr("transform", `translate(${marginLeft},0)`)
      .call(
        d3.axisLeft(y)
          .tickValues(d3.range(0, 36, 5))
      )
      .call(g => g.select(".domain").remove())
      .call(g => g.append("text")
          .attr("transform", "rotate(-90)")
          .attr("x", -(height / 2) + 5)
          .attr("y", -35 + 5)
          .attr("fill", "currentColor")
          .attr("text-anchor", "middle")
          .text("Average of Miles per Gallon"))

  svg.append("path")
      .datum(carsYearly)
      .attr("fill", "none")
      .attr("stroke", "#4c78a8")
      .attr("stroke-width", 1.5)
      .attr("d", line);

  return svg.node();
}"""
vega_lite_code = """
Plot.plot({
  width: 400,
  height: 300,
  
  x: {
    label: "Year",
    grid: false,
    line: true,
    labelAnchor: "center",
    labelArrow: "none", 
    tickFormat: "d",
    domain: [1970, 1982]
  },

  y: {
    label: "Average of Miles per Gallon",
    grid: false,
    labelAnchor: "center",
    labelArrow: "none", 
    domain: [0, 35]
  },

  marks: [
    Plot.lineY(carsYearly, {
      x: "Year",
      y: "Average_MPG",
      stroke: "#4c78a8"
    })
  ]
})"""

formatter = HtmlFormatter(
    noclasses=True, 
    style='one-dark', 
    prestyles="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;"
)

left_html = highlight(d3_code, JavascriptLexer(), formatter)
right_html = highlight(vega_lite_code, JsonLexer(), formatter)

final_output = f"""
<div style="display: flex; gap: 15px; width: 100%; align-items: stretch;">
  <div style="flex: 1; min-width: 0; overflow: hidden;">
    {left_html}
  </div>
  <div style="flex: 1; min-width: 0; overflow: hidden;">
    {right_html}
  </div>
</div>
"""

with open("LINE_D3_Observable.md", "w") as f:
    f.write(final_output)