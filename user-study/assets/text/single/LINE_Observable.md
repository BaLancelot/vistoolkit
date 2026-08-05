<div style="display: flex; gap: 20px; width: 100%; align-items: flex-start;">
  
  <div style="flex: 1; padding: 15px; background: white; border-radius: 6px;">
    <img src="user-study/assets/images/LINE_Observable.svg" alt="Vega-Lite Bar Chart" style="max-width: 100%; height: auto;" />
  </div>
  
  <div style="flex: 1; min-width: 0;">
  <div style="font-family: sans-serif; font-size: 18px; font-weight: bold; margin-bottom: 12px; color: #333;">
    Observable
  </div>
    <pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px !important; margin: 0; max-height: 500px; overflow-y: auto; white-space: pre;">
      <div style="flex: 1; min-width: 0; overflow: hidden;">
    <div class="highlight" style="background: #282C34"><pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px !important; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;; line-height: 125%;"><span></span><span style="color: #E06C75">Plot</span><span style="color: #E06C75">.plot</span><span style="color: #ABB2BF">({</span>
<span style="color: #E06C75">  width: </span><span style="color: #D19A66">400</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">  height</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">300</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span>
<span style="color: #E06C75">  x: </span><span style="color: #ABB2BF">{</span>
<span style="color: #E06C75">    label: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    grid: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    line</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    labelAnchor: </span><span style="color: #98C379">&quot;center&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    labelArrow: </span><span style="color: #98C379">&quot;none&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">tickFormat</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;d&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    domain</span><span style="color: #ABB2BF">: [</span><span style="color: #D19A66">1970</span><span style="color: #ABB2BF">, </span><span style="color: #D19A66">1982</span><span style="color: #ABB2BF">]</span>
<span style="color: #ABB2BF">  },</span>

<span style="color: #E06C75">  y: </span><span style="color: #ABB2BF">{</span>
<span style="color: #E06C75">    label: </span><span style="color: #98C379">&quot;Average of Miles per Gallon&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    grid: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    labelAnchor: </span><span style="color: #98C379">&quot;center&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">    labelArrow: </span><span style="color: #98C379">&quot;none&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #E06C75">    domain</span><span style="color: #ABB2BF">: [</span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">, </span><span style="color: #D19A66">35</span><span style="color: #ABB2BF">]</span>
<span style="color: #ABB2BF">  },</span>

<span style="color: #E06C75">  marks: </span><span style="color: #ABB2BF">[</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">Plot</span><span style="color: #E06C75">.lineY</span><span style="color: #ABB2BF">(</span><span style="color: #E06C75">carsYearly</span><span style="color: #ABB2BF">, {</span>
<span style="color: #E06C75">      x: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">      y: </span><span style="color: #98C379">&quot;Average_MPG&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #E06C75">      stroke: </span><span style="color: #98C379">&quot;#4c78a8&quot;</span>
<span style="color: #ABB2BF">    })</span>
<span style="color: #ABB2BF">  ]</span>
<span style="color: #ABB2BF">})</span>
</pre></div>

  </div>
</div>