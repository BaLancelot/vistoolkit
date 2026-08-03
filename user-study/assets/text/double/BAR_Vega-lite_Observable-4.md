<div style="margin-bottom: 15px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; color: #1F2328;">
  Is there anything else you would like to share about your experience reading and comparing the two code examples?
</div>
<div style="display: flex; gap: 15px; width: 100%; align-items: stretch;">
<div style="flex: 1; min-width: 0; overflow: hidden;">
    <div class="highlight" style="background: #282C34"><pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size !important: 13px; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;; line-height: 125%;"><span></span><span style="color: #ABB2BF">render({</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;$schema&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;https://vega.github.io/schema/vega-lite/v6.json&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;description&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;A simple bar chart with embedded data.&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;width&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">400</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;height&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">500</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;values&quot;</span><span style="color: #ABB2BF">: barData</span>
<span style="color: #ABB2BF">  },</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;mark&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;bar&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;color&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;#4c78a8&quot;</span>
<span style="color: #ABB2BF">  },</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;encoding&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;x&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;letter&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;nominal&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;axis&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;labelAngle&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;title&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Letter&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;tickColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;domainColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span>
<span style="color: #ABB2BF">          }</span>
<span style="color: #ABB2BF">         },</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;y&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;frequency&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;quantitative&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;axis&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;grid&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;title&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Count&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;domain&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;tickColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span>
<span style="color: #ABB2BF">      }</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  }, </span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;config&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;view&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;stroke&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">null</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  }</span>
<span style="color: #ABB2BF">})</span>
</pre></div>

  </div>

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
