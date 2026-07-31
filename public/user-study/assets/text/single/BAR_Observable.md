<div style="display: flex; gap: 20px; width: 100%; align-items: flex-start;">
  
  <div style="flex: 1; padding: 15px; background: white; border-radius: 6px;">
    <img src="user-study/assets/images/BAR_Observable.svg" alt="Vega-Lite Bar Chart" style="max-width: 100%; height: auto;" />
  </div>

  <div style="flex: 1; min-width: 0;">
    <pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px !important; margin: 0; max-height: 500px; overflow-y: auto; white-space: pre;">
      <div style="flex: 1; min-width: 0; overflow: hidden;">
    <div class="highlight" style="background: #282C34"><pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size !important: 13px; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;; line-height: 125%;"><span></span><span style="color: #ABB2BF">Plot</span><span style="color: #ABB2BF">.plot</span><span style="color: #ABB2BF">({</span>
<span style="color: #ABB2BF">  width: </span><span style="color: #D19A66">400</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  height</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">500</span><span style="color: #ABB2BF">,</span>

<span style="color: #ABB2BF">  x: {</span>
<span style="color: #ABB2BF">    label: </span><span style="color: #98C379">&quot;Letter&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    </span><span style="color: #E5C07B">tickRotate</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    line</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span>
<span style="color: #ABB2BF">  },</span>

<span style="color: #ABB2BF">  y: {</span>
<span style="color: #ABB2BF">    label: </span><span style="color: #98C379">&quot;Count&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    grid: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    line</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    labelAnchor: </span><span style="color: #98C379">&quot;center&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    labelArrow: </span><span style="color: #98C379">&quot;none&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    domain</span><span style="color: #ABB2BF">: [</span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">, </span><span style="color: #D19A66">100</span><span style="color: #ABB2BF">]</span>
<span style="color: #ABB2BF">  },</span>

<span style="color: #ABB2BF">  marks: [</span>
<span style="color: #ABB2BF">    Plot</span><span style="color: #ABB2BF">.barY(barData</span><span style="color: #ABB2BF">, {</span>
<span style="color: #ABB2BF">      x: </span><span style="color: #98C379">&quot;letter&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      y: </span><span style="color: #98C379">&quot;frequency&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E5C07B">fill: </span><span style="color: #98C379">&quot;#4c78a8&quot;</span>
<span style="color: #ABB2BF">    })</span>
<span style="color: #ABB2BF">  ]</span>
<span style="color: #ABB2BF">})</span>
</pre></div>

  </div>
</div>
