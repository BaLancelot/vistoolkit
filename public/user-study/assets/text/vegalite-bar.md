<div style="display: flex; gap: 20px; width: 100%;">

  <div style="flex: 1; min-width: 0;">
    <pre style="background-color: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 6px; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.5; overflow-x: auto; border: 1px solid #333; margin: 0; height: 100%;"><code><span style="color: #DCDCAA;">render</span>({ 
  <span style="color: #9CDCFE;">"$schema"</span>: <span style="color: #CE9178;">"https://vega.github.io/schema/vega-lite/v6.json"</span>,
  <span style="color: #9CDCFE;">"description"</span>: <span style="color: #CE9178;">"A simple bar chart."</span>,
  <span style="color: #9CDCFE;">"width"</span>: <span style="color: #B5CEA8;">400</span>,
  <span style="color: #9CDCFE;">"height"</span>: <span style="color: #B5CEA8;">500</span>,
  <span style="color: #9CDCFE;">"data"</span>: { <span style="color: #9CDCFE;">"values"</span>: [ {<span style="color: #9CDCFE;">"a"</span>: <span style="color: #CE9178;">"A"</span>, <span style="color: #9CDCFE;">"b"</span>: <span style="color: #B5CEA8;">28</span>} ] },
  <span style="color: #9CDCFE;">"mark"</span>: <span style="color: #CE9178;">"bar"</span>,
  <span style="color: #9CDCFE;">"encoding"</span>: {
    <span style="color: #9CDCFE;">"x"</span>: {<span style="color: #9CDCFE;">"field"</span>: <span style="color: #CE9178;">"a"</span>, <span style="color: #9CDCFE;">"type"</span>: <span style="color: #CE9178;">"nominal"</span>},
    <span style="color: #9CDCFE;">"y"</span>: {<span style="color: #9CDCFE;">"field"</span>: <span style="color: #CE9178;">"b"</span>, <span style="color: #9CDCFE;">"type"</span>: <span style="color: #CE9178;">"quantitative"</span>}
  }
})</code></pre>
  </div>

  <div style="flex: 1; min-width: 0;">
    <pre style="background-color: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 6px; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.5; overflow-x: auto; border: 1px solid #333; margin: 0; height: 100%;"><code><span style="color: #9CDCFE;">barChart</span> = {
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">width</span> = <span style="color: #B5CEA8;">400</span>;
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">height</span> = <span style="color: #B5CEA8;">500</span>;
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">marginTop</span> = <span style="color: #B5CEA8;">30</span>;
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">marginRight</span> = <span style="color: #B5CEA8;">0</span>;
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">marginBottom</span> = <span style="color: #B5CEA8;">40</span>;
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">marginLeft</span> = <span style="color: #B5CEA8;">50</span>;

  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">sortedData</span> = <span style="color: #9CDCFE;">barData</span>.<span style="color: #DCDCAA;">slice</span>().<span style="color: #DCDCAA;">sort</span>((<span style="color: #9CDCFE;">a</span>, <span style="color: #9CDCFE;">b</span>) =&gt; <span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">ascending</span>(<span style="color: #9CDCFE;">a</span>.<span style="color: #9CDCFE;">letter</span>, <span style="color: #9CDCFE;">b</span>.<span style="color: #9CDCFE;">letter</span>));

  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">x</span> = <span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">scaleBand</span>()
      .<span style="color: #DCDCAA;">domain</span>(<span style="color: #9CDCFE;">sortedData</span>.<span style="color: #DCDCAA;">map</span>(<span style="color: #9CDCFE;">d</span> =&gt; <span style="color: #9CDCFE;">d</span>.<span style="color: #9CDCFE;">letter</span>))
      .<span style="color: #DCDCAA;">range</span>([<span style="color: #9CDCFE;">marginLeft</span>, <span style="color: #9CDCFE;">width</span> - <span style="color: #9CDCFE;">marginRight</span>])
      .<span style="color: #DCDCAA;">padding</span>(<span style="color: #B5CEA8;">0.1</span>);
  
  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">y</span> = <span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">scaleLinear</span>()
      .<span style="color: #DCDCAA;">domain</span>([<span style="color: #B5CEA8;">0</span>, <span style="color: #B5CEA8;">100</span>])
      .<span style="color: #DCDCAA;">nice</span>()
      .<span style="color: #DCDCAA;">range</span>([<span style="color: #9CDCFE;">height</span> - <span style="color: #9CDCFE;">marginBottom</span>, <span style="color: #9CDCFE;">marginTop</span>]);

  <span style="color: #569CD6;">const</span> <span style="color: #4FC1FF;">svg</span> = <span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">create</span>(<span style="color: #CE9178;">"svg"</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"width"</span>, <span style="color: #9CDCFE;">width</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"height"</span>, <span style="color: #9CDCFE;">height</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"viewBox"</span>, [<span style="color: #B5CEA8;">0</span>, <span style="color: #B5CEA8;">0</span>, <span style="color: #9CDCFE;">width</span>, <span style="color: #9CDCFE;">height</span>])
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"style"</span>, <span style="color: #CE9178;">"max-width: 100%; height: auto;"</span>);

  <span style="color: #9CDCFE;">svg</span>.<span style="color: #DCDCAA;">append</span>(<span style="color: #CE9178;">"g"</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"fill"</span>, <span style="color: #CE9178;">"#4c78a8"</span>)
    .<span style="color: #DCDCAA;">selectAll</span>()
    .<span style="color: #DCDCAA;">data</span>(<span style="color: #9CDCFE;">sortedData</span>)
    .<span style="color: #DCDCAA;">join</span>(<span style="color: #CE9178;">"rect"</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"x"</span>, <span style="color: #9CDCFE;">d</span> =&gt; <span style="color: #DCDCAA;">x</span>(<span style="color: #9CDCFE;">d</span>.<span style="color: #9CDCFE;">letter</span>))
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"y"</span>, <span style="color: #9CDCFE;">d</span> =&gt; <span style="color: #DCDCAA;">y</span>(<span style="color: #9CDCFE;">d</span>.<span style="color: #9CDCFE;">frequency</span>))
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"height"</span>, <span style="color: #9CDCFE;">d</span> =&gt; <span style="color: #DCDCAA;">y</span>(<span style="color: #B5CEA8;">0</span>) - <span style="color: #DCDCAA;">y</span>(<span style="color: #9CDCFE;">d</span>.<span style="color: #9CDCFE;">frequency</span>))
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"width"</span>, <span style="color: #9CDCFE;">x</span>.<span style="color: #DCDCAA;">bandwidth</span>());

  <span style="color: #9CDCFE;">svg</span>.<span style="color: #DCDCAA;">append</span>(<span style="color: #CE9178;">"g"</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"transform"</span>, <span style="color: #CE9178;">`translate(0,${</span><span style="color: #9CDCFE;">height</span> - <span style="color: #9CDCFE;">marginBottom</span><span style="color: #CE9178;">})`</span>)
      .<span style="color: #DCDCAA;">call</span>(<span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">axisBottom</span>(<span style="color: #9CDCFE;">x</span>).<span style="color: #DCDCAA;">tickSizeOuter</span>(<span style="color: #B5CEA8;">0</span>))
      .<span style="color: #DCDCAA;">call</span>(<span style="color: #9CDCFE;">g</span> =&gt; <span style="color: #9CDCFE;">g</span>.<span style="color: #DCDCAA;">append</span>(<span style="color: #CE9178;">"text"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"x"</span>, (<span style="color: #9CDCFE;">width</span> - <span style="color: #9CDCFE;">marginLeft</span> - <span style="color: #9CDCFE;">marginRight</span>) / <span style="color: #B5CEA8;">2</span> + <span style="color: #9CDCFE;">marginLeft</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"y"</span>, <span style="color: #B5CEA8;">32</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"fill"</span>, <span style="color: #CE9178;">"currentColor"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"text-anchor"</span>, <span style="color: #CE9178;">"middle"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"font-size"</span>, <span style="color: #CE9178;">"11px"</span>)
          .<span style="color: #DCDCAA;">text</span>(<span style="color: #CE9178;">"Letter"</span>));

  <span style="color: #9CDCFE;">svg</span>.<span style="color: #DCDCAA;">append</span>(<span style="color: #CE9178;">"g"</span>)
      .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"transform"</span>, <span style="color: #CE9178;">`translate(${</span><span style="color: #9CDCFE;">marginLeft</span><span style="color: #CE9178;">},0)`</span>)
      .<span style="color: #DCDCAA;">call</span>(<span style="color: #9CDCFE;">d3</span>.<span style="color: #DCDCAA;">axisLeft</span>(<span style="color: #9CDCFE;">y</span>))
      .<span style="color: #DCDCAA;">call</span>(<span style="color: #9CDCFE;">g</span> =&gt; <span style="color: #9CDCFE;">g</span>.<span style="color: #DCDCAA;">select</span>(<span style="color: #CE9178;">".domain"</span>).<span style="color: #DCDCAA;">remove</span>())
      .<span style="color: #DCDCAA;">call</span>(<span style="color: #9CDCFE;">g</span> =&gt; <span style="color: #9CDCFE;">g</span>.<span style="color: #DCDCAA;">append</span>(<span style="color: #CE9178;">"text"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"transform"</span>, <span style="color: #CE9178;">"rotate(-90)"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"x"</span>, -(<span style="color: #9CDCFE;">height</span> / <span style="color: #B5CEA8;">2</span>) + <span style="color: #B5CEA8;">5</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"y"</span>, -<span style="color: #B5CEA8;">32</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"fill"</span>, <span style="color: #CE9178;">"currentColor"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"text-anchor"</span>, <span style="color: #CE9178;">"middle"</span>)
          .<span style="color: #DCDCAA;">attr</span>(<span style="color: #CE9178;">"font-size"</span>, <span style="color: #CE9178;">"11px"</span>)
          .<span style="color: #DCDCAA;">text</span>(<span style="color: #CE9178;">"Count"</span>))

  <span style="color: #569CD6;">return</span> <span style="color: #9CDCFE;">svg</span>.<span style="color: #DCDCAA;">node</span>();
}</code></pre>
  </div>

</div>