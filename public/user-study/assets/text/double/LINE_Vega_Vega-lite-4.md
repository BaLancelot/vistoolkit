<div style="margin-bottom: 15px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; color: #1F2328;">
  Is there anything else you would like to share about your experience reading and comparing the two code examples?
</div>
<div style="display: flex; gap: 15px; width: 100%; align-items: stretch;">
<div style="flex: 1; min-width: 0; overflow: hidden;">
<div style="background-color: #21252b; color: #abb2bf; padding: 10px 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; font-weight: 600; border-bottom: 1px solid #3e4451;">
      Vega
    </div>
    <div class="highlight" style="background: #282C34"><pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px !important; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;; line-height: 125%;"><span></span><span style="color: #C678DD">viewof</span><span style="color: #ABB2BF"> </span><span style="color: #E06C75">lineView</span><span style="color: #ABB2BF"> </span><span style="color: #56B6C2">=</span><span style="color: #ABB2BF"> </span><span style="color: #E06C75">embed</span><span style="color: #ABB2BF">({</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;$schema&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;https://vega.github.io/schema/vega/v6.json&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;background&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;white&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;padding&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">5</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;width&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">320</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;height&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">240</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;style&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;cell&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: [</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;name&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;source_0&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;values&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E06C75">carsYearly</span>
<span style="color: #ABB2BF">    },</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;name&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;data_0&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;source&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;source_0&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;transform&quot;</span><span style="color: #ABB2BF">: [</span>
<span style="color: #ABB2BF">        {</span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;formula&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;expr&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;toNumber(datum[&#92&quot;Year&#92&quot;])&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;as&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">}</span>
<span style="color: #ABB2BF">      ]</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  ],</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;marks&quot;</span><span style="color: #ABB2BF">: [</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;name&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;marks&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;line&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;style&quot;</span><span style="color: #ABB2BF">: [</span><span style="color: #98C379">&quot;line&quot;</span><span style="color: #ABB2BF">],</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;sort&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;x&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;from&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;data_0&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;encode&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;update&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;stroke&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;value&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;#4c78a8&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;strokeWidth&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;value&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">1.3</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;description&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;&#92&quot;Year: &#92&quot; + (format(datum[&#92&quot;Year&#92&quot;], &#92&quot;d&#92&quot;)) + &#92&quot;; Average of Miles per Gallon: &#92&quot; + (format(datum[&#92&quot;Average_MPG&#92&quot;], &#92&quot;&#92&quot;))&quot;</span>
<span style="color: #ABB2BF">          },</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;x&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;scale&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;x&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;y&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;scale&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;y&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Average_MPG&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;defined&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;isValid(datum[&#92&quot;Year&#92&quot;]) &amp;&amp; isFinite(+datum[&#92&quot;Year&#92&quot;]) &amp;&amp; isValid(datum[&#92&quot;Average_MPG&#92&quot;]) &amp;&amp; isFinite(+datum[&#92&quot;Average_MPG&#92&quot;])&quot;</span>
<span style="color: #ABB2BF">          }</span>
<span style="color: #ABB2BF">        }</span>
<span style="color: #ABB2BF">      }</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  ],</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;scales&quot;</span><span style="color: #ABB2BF">: [</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;name&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;x&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;linear&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;domain&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;data_0&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;range&quot;</span><span style="color: #ABB2BF">: [</span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">, {</span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;width&quot;</span><span style="color: #ABB2BF">}],</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;nice&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;zero&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span>
<span style="color: #ABB2BF">    },</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;name&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;y&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;linear&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;domain&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;data_0&quot;</span><span style="color: #ABB2BF">, </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Average_MPG&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;range&quot;</span><span style="color: #ABB2BF">: [{</span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;height&quot;</span><span style="color: #ABB2BF">}, </span><span style="color: #D19A66">0</span><span style="color: #ABB2BF">],</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;nice&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;zero&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  ],</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;axes&quot;</span><span style="color: #ABB2BF">: [</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;scale&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;x&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;orient&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;bottom&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;grid&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;title&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;domainColor&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;tickColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;format&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;d&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;tickMinStep&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">2</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;labelFlush&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;labelOverlap&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;tickCount&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;ceil(width/40)&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;zindex&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">0</span>
<span style="color: #ABB2BF">    },</span>
<span style="color: #ABB2BF">    {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;scale&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;y&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;orient&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;left&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;grid&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;title&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Average of Miles per Gallon&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;domain&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;labelOverlap&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">true</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;tickCount&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;signal&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;ceil(height/40)&quot;</span><span style="color: #ABB2BF">},</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;zindex&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">0</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  ],</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;config&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;style&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;cell&quot;</span><span style="color: #ABB2BF">: {</span><span style="color: #E06C75">&quot;stroke&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">null</span><span style="color: #ABB2BF">}}}</span>
<span style="color: #ABB2BF">})</span>
</pre></div>

  </div>
<div style="flex: 1; min-width: 0;">
      <div style="flex: 1; min-width: 0; overflow: hidden;">
      <div style="background-color: #21252b; color: #abb2bf; padding: 10px 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; font-weight: 600; border-bottom: 1px solid #3e4451;">
      Vega-Lite
    </div>
    <div class="highlight" style="background: #282C34"><pre style="background-color: #282c34; color: #abb2bf; padding: 16px; border-radius: 6px; font-family: 'Consolas', monospace; font-size: 13px !important; line-height: 1.5; overflow-x: auto; border: 1px solid #3e4451; margin: 0; box-sizing: border-box;; line-height: 125%;"><span></span><span style="color: #E06C75">render</span><span style="color: #ABB2BF">({</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;$schema&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;https://vega.github.io/schema/vega-lite/v6.json&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;width&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">320</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;height&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">240</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;mark&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;line&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;color&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;#4c78a8&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;strokeWidth&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #D19A66">1.5</span>
<span style="color: #ABB2BF">  },</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;data&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;values&quot;</span><span style="color: #E06C75"> : carsYearly</span>
<span style="color: #ABB2BF">  },</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;encoding&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;x&quot;</span><span style="color: #ABB2BF">: { </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Year&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;quantitative&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">          </span><span style="color: #E06C75">&quot;axis&quot;</span><span style="color: #ABB2BF"> : {</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;grid&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;domainColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;tickColor&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;black&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;format&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;d&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;tickMinStep&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #D19A66">2</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;labelFlush&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #E5C07B">false</span>
<span style="color: #ABB2BF">          }</span>
<span style="color: #ABB2BF">         },</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;y&quot;</span><span style="color: #ABB2BF">: { </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;field&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;Average_MPG&quot;</span><span style="color: #ABB2BF">, </span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;type&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;quantitative&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;title&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #98C379">&quot;Average of Miles per Gallon&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;axis&quot;</span><span style="color: #ABB2BF"> : {</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;grid&quot;</span><span style="color: #ABB2BF"> : </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;titleFontWeight&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #98C379">&quot;normal&quot;</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">            </span><span style="color: #E06C75">&quot;domain&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">false</span><span style="color: #ABB2BF">,</span>
<span style="color: #ABB2BF">          }</span>
<span style="color: #ABB2BF">        }</span>
<span style="color: #ABB2BF">  },</span>
<span style="color: #ABB2BF">  </span><span style="color: #E06C75">&quot;config&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">    </span><span style="color: #E06C75">&quot;style&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">      </span><span style="color: #E06C75">&quot;cell&quot;</span><span style="color: #ABB2BF">: {</span>
<span style="color: #ABB2BF">        </span><span style="color: #E06C75">&quot;stroke&quot;</span><span style="color: #ABB2BF">: </span><span style="color: #E5C07B">null</span>
<span style="color: #ABB2BF">      }</span>
<span style="color: #ABB2BF">    }</span>
<span style="color: #ABB2BF">  }</span>
<span style="color: #ABB2BF">})</span>
</pre></div>

  </div>
</div>