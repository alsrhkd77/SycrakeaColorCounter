# 시카라키아 색깔 카운터

> python 3.10
> 시카라키아 색깔 패턴 보조를 위한 카운터 프로그램

오버레이 기능 및 단축키를 통한 제어 기능

## 다운로드

https://github.com/HwanSangYeonHwa/SycrakeaColorCounter/releases/latest

## 기능

- `+`버튼, `-`버튼을 통한 카운터 숫자 증감
- `오버레이 모드` 버튼을 통한 오버레이 활성화
- 단축키를 통한 숫자 증감
- 단축키를 통한 오버레이 비활성화 및 프로그램 종료
- `config.json`을 통한 설정 적용

## 실행

`SycrakeaColorCounter` 또는 `SycrakeaColorCounter.exe`를 `관리자 권한`으로 실행합니다.

실행 파일과 같은 폴더에 `config.json`파일이 있을 경우 설정을 적용할 수 있습니다.

## 기본 단축키

> 단축키는 설정 파일에서 변경할 수 있습니다.

단축키는 모두 `ALT`+ 영문으로 이루어져 있습니다.

- `ALT + A` 빨강 숫자 증가
- `ALT + S` 파랑 숫자 증가
- `ALT + D` 노랑 숫자 증가
- `ALT + F` 하양 숫자 증가
- `ALT + E` 카운터 숫자 초기화
- `ALT + O` 오버레이 비활성화
- `ALT + Q` 프로그램 종료

## 설정

설정은 `config.json` 파일에서 변경할 수 있습니다.

- `colors` 각 칸에 보여질 색상에 대한 설정입니다. 4가지 색을 설정할 수 있으며 첫 번째 색상이 가장 왼쪽 칸에 적용되는 색상입니다. `,`로 구분됩니다.
- `font_colors` 각 칸에 쓰여지는 폰트의 색상입니다. 4가지 색을 설정할 수 있으며 첫 번째 색상이 가장 왼쪽 칸에 적용되는 색상입니다. `,`로 구분됩니다.
- `hot_keys` 이벤트를 감지할 Key에 대한 설정입니다. `+`를 사용해 여러 키 조합을 사용할 수 있으며 특수키는 `<>`를 사용해 설정합니다.
  - `colors_n+` n번째 칸의 숫자를 증가
  - `colors_n-` n번째 칸의 숫자를 감소
  - `reset` 모든 칸의 숫자를 0으로 초기화
  - `toggle_overlay` 오버레이 모드 토글
  - `exit_program` 종료
- `overlay_alpha` 오버레이 모드 창 투명도에 대한 설정입니다. (0.0 ~ 1.0)

<details>
<summary>사용 가능한 특수키</summary>

- alt

- alt_gr

- alt_l

- alt_r

- backspace

- caps_lock

- cmd

- cmd_l

- cmd_r

- ctrl

- ctrl_l

- ctrl_r

- delete

- down

- end

- enter

- esc

- f1 ~ f20

- home

- insert

- left

- media_next

- media_play_pause

- media_previous

- media_volume_down

- media_volume_mute

- media_volume_up

- menu

- num_lock

- page_down

- page_up

- pause

- print_screen

- right

- scroll_lock

- shift

- shift_l

- shift_r

- space

- tab

- up

</details>

<details>
<summary>적용 가능한 색상 목록</summary>
    <table class="table"><tbody><tr><th>Name </th><th>Red </th><th>Green </th><th>Blue</th><th> HEX </th></tr>
    <tr bgcolor="#F0F0F8"><td>alice blue </td><td>240 </td><td>248 </td><td>255</td><td> #F0F0F8</td></tr>
    <tr bgcolor="#F0F0F8"><td>AliceBlue </td><td>240 </td><td>248 </td><td>255</td><td> #F0F0F8</td></tr>
    <tr bgcolor="#FAFAEB"><td>antique white </td><td>250 </td><td>235 </td><td>215</td><td> #FAFAEB</td></tr>
    <tr bgcolor="#FAFAEB"><td>AntiqueWhite </td><td>250 </td><td>235 </td><td>215</td><td> #FAFAEB</td></tr>
    <tr bgcolor="#FFFFEF"><td>AntiqueWhite1 </td><td>255 </td><td>239 </td><td>219</td><td> #FFFFEF</td></tr>
    <tr bgcolor="#EEEEDF"><td>AntiqueWhite2 </td><td>238 </td><td>223 </td><td>204</td><td> #EEEEDF</td></tr>
    <tr bgcolor="#CDCDC0"><td>AntiqueWhite3 </td><td>205 </td><td>192 </td><td>176</td><td> #CDCDC0</td></tr>
    <tr bgcolor="#8B8B83"><td>AntiqueWhite4 </td><td>139 </td><td>131 </td><td>120</td><td> #8B8B83</td></tr>
    <tr bgcolor="#0000FF"><td>agua </td><td>0 </td><td>255 </td><td>255</td><td> #0000FF</td></tr>
    <tr bgcolor="#7F7FFF"><td>aquamarine </td><td>127 </td><td>255 </td><td>212</td><td> #7F7FFF</td></tr>
    <tr bgcolor="#7F7FFF"><td>aquamarine1 </td><td>127 </td><td>255 </td><td>212</td><td> #7F7FFF</td></tr>
    <tr bgcolor="#7676EE"><td>aquamarine2 </td><td>118 </td><td>238 </td><td>198</td><td> #7676EE</td></tr>
    <tr bgcolor="#6666CD"><td>aquamarine3 </td><td>102 </td><td>205 </td><td>170</td><td> #6666CD</td></tr>
    <tr bgcolor="#45458B"><td>aquamarine4 </td><td>69 </td><td>139 </td><td>116</td><td> #45458B</td></tr>
    <tr bgcolor="#F0F0FF"><td>azure </td><td>240 </td><td>255 </td><td>255</td><td> #F0F0FF</td></tr>
    <tr bgcolor="#F0F0FF"><td>azure1 </td><td>240 </td><td>255 </td><td>255</td><td> #F0F0FF</td></tr>
    <tr bgcolor="#E0E0EE"><td>azure2 </td><td>224 </td><td>238 </td><td>238</td><td> #E0E0EE</td></tr>
    <tr bgcolor="#C1C1CD"><td>azure3 </td><td>193 </td><td>205 </td><td>205</td><td> #C1C1CD</td></tr>
    <tr bgcolor="#83838B"><td>azure4 </td><td>131 </td><td>139 </td><td>139</td><td> #83838B</td></tr>
    <tr bgcolor="#F5F5F5"><td>beige </td><td>245 </td><td>245 </td><td>220</td><td> #F5F5F5</td></tr>
    <tr bgcolor="#FFFFE4"><td>bisque </td><td>255 </td><td>228 </td><td>196</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#FFFFE4"><td>bisque1 </td><td>255 </td><td>228 </td><td>196</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#EEEED5"><td>bisque2 </td><td>238 </td><td>213 </td><td>183</td><td> #EEEED5</td></tr>
    <tr bgcolor="#CDCDB7"><td>bisque3 </td><td>205 </td><td>183 </td><td>158</td><td> #CDCDB7</td></tr>
    <tr bgcolor="#8B8B7D"><td>bisque4 </td><td>139 </td><td>125 </td><td>107</td><td> #8B8B7D</td></tr>
    <tr bgcolor="#000000"><td>black </td><td>0 </td><td>0 </td><td>0</td><td> #000000</td></tr>
    <tr bgcolor="#FFFFEB"><td>blanched almond </td><td>255 </td><td>235 </td><td>205</td><td> #FFFFEB</td></tr>
    <tr bgcolor="#FFFFEB"><td>BlanchedAlmond </td><td>255 </td><td>235 </td><td>205</td><td> #FFFFEB</td></tr>
    <tr bgcolor="#000000"><td>blue </td><td>0 </td><td>0 </td><td>255</td><td> #000000</td></tr>
    <tr bgcolor="#8A8A2B"><td>blue violet </td><td>138 </td><td>43 </td><td>226</td><td> #8A8A2B</td></tr>
    <tr bgcolor="#000000"><td>blue1 </td><td>0 </td><td>0 </td><td>255</td><td> #000000</td></tr>
    <tr bgcolor="#000000"><td>blue2 </td><td>0 </td><td>0 </td><td>238</td><td> #000000</td></tr>
    <tr bgcolor="#000000"><td>blue3 </td><td>0 </td><td>0 </td><td>205</td><td> #000000</td></tr>
    <tr bgcolor="#000000"><td>blue4 </td><td>0 </td><td>0 </td><td>139</td><td> #000000</td></tr>
    <tr bgcolor="#8A8A2B"><td>BlueViolet </td><td>138 </td><td>43 </td><td>226</td><td> #8A8A2B</td></tr>
    <tr bgcolor="#A5A52A"><td>brown </td><td>165 </td><td>42 </td><td>42</td><td> #A5A52A</td></tr>
    <tr bgcolor="#FFFF40"><td>brown1 </td><td>255 </td><td>64 </td><td>64</td><td> #FFFF40</td></tr>
    <tr bgcolor="#EEEE3B"><td>brown2 </td><td>238 </td><td>59 </td><td>59</td><td> #EEEE3B</td></tr>
    <tr bgcolor="#CDCD33"><td>brown3 </td><td>205 </td><td>51 </td><td>51</td><td> #CDCD33</td></tr>
    <tr bgcolor="#8B8B23"><td>brown4 </td><td>139 </td><td>35 </td><td>35</td><td> #8B8B23</td></tr>
    <tr bgcolor="#DEDEB8"><td>burlywood </td><td>222 </td><td>184 </td><td>135</td><td> #DEDEB8</td></tr>
    <tr bgcolor="#FFFFD3"><td>burlywood1 </td><td>255 </td><td>211 </td><td>155</td><td> #FFFFD3</td></tr>
    <tr bgcolor="#EEEEC5"><td>burlywood2 </td><td>238 </td><td>197 </td><td>145</td><td> #EEEEC5</td></tr>
    <tr bgcolor="#CDCDAA"><td>burlywood3 </td><td>205 </td><td>170 </td><td>125</td><td> #CDCDAA</td></tr>
    <tr bgcolor="#8B8B73"><td>burlywood4 </td><td>139 </td><td>115 </td><td>85</td><td> #8B8B73</td></tr>
    <tr bgcolor="#5F5F9E"><td>cadet blue </td><td>95 </td><td>158 </td><td>160</td><td> #5F5F9E</td></tr>
    <tr bgcolor="#5F5F9E"><td>CadetBlue </td><td>95 </td><td>158 </td><td>160</td><td> #5F5F9E</td></tr>
    <tr bgcolor="#9898F5"><td>CadetBlue1 </td><td>152 </td><td>245 </td><td>255</td><td> #9898F5</td></tr>
    <tr bgcolor="#8E8EE5"><td>CadetBlue2 </td><td>142 </td><td>229 </td><td>238</td><td> #8E8EE5</td></tr>
    <tr bgcolor="#7A7AC5"><td>CadetBlue3 </td><td>122 </td><td>197 </td><td>205</td><td> #7A7AC5</td></tr>
    <tr bgcolor="#535386"><td>CadetBlue4 </td><td>83 </td><td>134 </td><td>139</td><td> #535386</td></tr>
    <tr bgcolor="#7F7FFF"><td>chartreuse </td><td>127 </td><td>255 </td><td>0</td><td> #7F7FFF</td></tr>
    <tr bgcolor="#7F7FFF"><td>chartreuse1 </td><td>127 </td><td>255 </td><td>0</td><td> #7F7FFF</td></tr>
    <tr bgcolor="#7676EE"><td>chartreuse2 </td><td>118 </td><td>238 </td><td>0</td><td> #7676EE</td></tr>
    <tr bgcolor="#6666CD"><td>chartreuse3 </td><td>102 </td><td>205 </td><td>0</td><td> #6666CD</td></tr>
    <tr bgcolor="#45458B"><td>chartreuse4 </td><td>69 </td><td>139 </td><td>0</td><td> #45458B</td></tr>
    <tr bgcolor="#D2D269"><td>chocolate </td><td>210 </td><td>105 </td><td>30</td><td> #D2D269</td></tr>
    <tr bgcolor="#FFFF7F"><td>chocolate1 </td><td>255 </td><td>127 </td><td>36</td><td> #FFFF7F</td></tr>
    <tr bgcolor="#EEEE76"><td>chocolate2 </td><td>238 </td><td>118 </td><td>33</td><td> #EEEE76</td></tr>
    <tr bgcolor="#CDCD66"><td>chocolate3 </td><td>205 </td><td>102 </td><td>29</td><td> #CDCD66</td></tr>
    <tr bgcolor="#8B8B45"><td>chocolate4 </td><td>139 </td><td>69 </td><td>19</td><td> #8B8B45</td></tr>
    <tr bgcolor="#FFFF7F"><td>coral </td><td>255 </td><td>127 </td><td>80</td><td> #FFFF7F</td></tr>
    <tr bgcolor="#FFFF72"><td>coral1 </td><td>255 </td><td>114 </td><td>86</td><td> #FFFF72</td></tr>
    <tr bgcolor="#EEEE6A"><td>coral2 </td><td>238 </td><td>106 </td><td>80</td><td> #EEEE6A</td></tr>
    <tr bgcolor="#CDCD5B"><td>coral3 </td><td>205 </td><td>91 </td><td>69</td><td> #CDCD5B</td></tr>
    <tr bgcolor="#8B8B3E"><td>coral4 </td><td>139 </td><td>62 </td><td>47</td><td> #8B8B3E</td></tr>
    <tr bgcolor="#646495"><td>cornflower blue </td><td>100 </td><td>149 </td><td>237</td><td> #646495</td></tr>
    <tr bgcolor="#646495"><td>CornflowerBlue </td><td>100 </td><td>149 </td><td>237</td><td> #646495</td></tr>
    <tr bgcolor="#FFFFF8"><td>cornsilk </td><td>255 </td><td>248 </td><td>220</td><td> #FFFFF8</td></tr>
    <tr bgcolor="#FFFFF8"><td>cornsilk1 </td><td>255 </td><td>248 </td><td>220</td><td> #FFFFF8</td></tr>
    <tr bgcolor="#EEEEE8"><td>cornsilk2 </td><td>238 </td><td>232 </td><td>205</td><td> #EEEEE8</td></tr>
    <tr bgcolor="#CDCDC8"><td>cornsilk3 </td><td>205 </td><td>200 </td><td>177</td><td> #CDCDC8</td></tr>
    <tr bgcolor="#8B8B88"><td>cornsilk4 </td><td>139 </td><td>136 </td><td>120</td><td> #8B8B88</td></tr>
    <tr bgcolor="#DCDC14"><td>crymson </td><td>220 </td><td>20 </td><td>60</td><td> #DCDC14</td></tr>
    <tr bgcolor="#0000FF"><td>cyan </td><td>0 </td><td>255 </td><td>255</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000FF"><td>cyan1 </td><td>0 </td><td>255 </td><td>255</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000EE"><td>cyan2 </td><td>0 </td><td>238 </td><td>238</td><td> #0000EE</td></tr>
    <tr bgcolor="#0000CD"><td>cyan3 </td><td>0 </td><td>205 </td><td>205</td><td> #0000CD</td></tr>
    <tr bgcolor="#00008B"><td>cyan4 </td><td>0 </td><td>139 </td><td>139</td><td> #00008B</td></tr>
    <tr bgcolor="#000000"><td>dark blue </td><td>0 </td><td>0 </td><td>139</td><td> #000000</td></tr>
    <tr bgcolor="#00008B"><td>dark cyan </td><td>0 </td><td>139 </td><td>139</td><td> #00008B</td></tr>
    <tr bgcolor="#B8B886"><td>dark goldenrod </td><td>184 </td><td>134 </td><td>11</td><td> #B8B886</td></tr>
    <tr bgcolor="#A9A9A9"><td>dark gray </td><td>169 </td><td>169 </td><td>169</td><td> #A9A9A9</td></tr>
    <tr bgcolor="#000064"><td>dark green </td><td>0 </td><td>100 </td><td>0</td><td> #000064</td></tr>
    <tr bgcolor="#A9A9A9"><td>dark grey </td><td>169 </td><td>169 </td><td>169</td><td> #A9A9A9</td></tr>
    <tr bgcolor="#BDBDB7"><td>dark khaki </td><td>189 </td><td>183 </td><td>107</td><td> #BDBDB7</td></tr>
    <tr bgcolor="#8B8B00"><td>dark magenta </td><td>139 </td><td>0 </td><td>139</td><td> #8B8B00</td></tr>
    <tr bgcolor="#55556B"><td>dark olive green </td><td>85 </td><td>107 </td><td>47</td><td> #55556B</td></tr>
    <tr bgcolor="#FFFF8C"><td>dark orange </td><td>255 </td><td>140 </td><td>0</td><td> #FFFF8C</td></tr>
    <tr bgcolor="#999932"><td>dark orchid </td><td>153 </td><td>50 </td><td>204</td><td> #999932</td></tr>
    <tr bgcolor="#8B8B00"><td>dark red </td><td>139 </td><td>0 </td><td>0</td><td> #8B8B00</td></tr>
    <tr bgcolor="#E9E996"><td>dark salmon </td><td>233 </td><td>150 </td><td>122</td><td> #E9E996</td></tr>
    <tr bgcolor="#8F8FBC"><td>dark sea green </td><td>143 </td><td>188 </td><td>143</td><td> #8F8FBC</td></tr>
    <tr bgcolor="#48483D"><td>dark slate blue </td><td>72 </td><td>61 </td><td>139</td><td> #48483D</td></tr>
    <tr bgcolor="#2F2F4F"><td>dark slate gray </td><td>47 </td><td>79 </td><td>79</td><td> #2F2F4F</td></tr>
    <tr bgcolor="#2F2F4F"><td>dark slate grey </td><td>47 </td><td>79 </td><td>79</td><td> #2F2F4F</td></tr>
    <tr bgcolor="#0000CE"><td>dark turquoise </td><td>0 </td><td>206 </td><td>209</td><td> #0000CE</td></tr>
    <tr bgcolor="#949400"><td>dark violet </td><td>148 </td><td>0 </td><td>211</td><td> #949400</td></tr>
    <tr bgcolor="#000000"><td>DarkBlue </td><td>0 </td><td>0 </td><td>139</td><td> #000000</td></tr>
    <tr bgcolor="#00008B"><td>DarkCyan </td><td>0 </td><td>139 </td><td>139</td><td> #00008B</td></tr>
    <tr bgcolor="#B8B886"><td>DarkGoldenrod </td><td>184 </td><td>134 </td><td>11</td><td> #B8B886</td></tr>
    <tr bgcolor="#FFFFB9"><td>DarkGoldenrod1 </td><td>255 </td><td>185 </td><td>15</td><td> #FFFFB9</td></tr>
    <tr bgcolor="#EEEEAD"><td>DarkGoldenrod2 </td><td>238 </td><td>173 </td><td>14</td><td> #EEEEAD</td></tr>
    <tr bgcolor="#CDCD95"><td>DarkGoldenrod3 </td><td>205 </td><td>149 </td><td>12</td><td> #CDCD95</td></tr>
    <tr bgcolor="#8B8B65"><td>DarkGoldenrod4 </td><td>139 </td><td>101 </td><td>8</td><td> #8B8B65</td></tr>
    <tr bgcolor="#A9A9A9"><td>DarkGray </td><td>169 </td><td>169 </td><td>169</td><td> #A9A9A9</td></tr>
    <tr bgcolor="#000064"><td>DarkGreen </td><td>0 </td><td>100 </td><td>0</td><td> #000064</td></tr>
    <tr bgcolor="#A9A9A9"><td>DarkGrey </td><td>169 </td><td>169 </td><td>169</td><td> #A9A9A9</td></tr>
    <tr bgcolor="#BDBDB7"><td>DarkKhaki </td><td>189 </td><td>183 </td><td>107</td><td> #BDBDB7</td></tr>
    <tr bgcolor="#8B8B00"><td>DarkMagenta </td><td>139 </td><td>0 </td><td>139</td><td> #8B8B00</td></tr>
    <tr bgcolor="#55556B"><td>DarkOliveGreen </td><td>85 </td><td>107 </td><td>47</td><td> #55556B</td></tr>
    <tr bgcolor="#CACAFF"><td>DarkOliveGreen1 </td><td>202 </td><td>255 </td><td>112</td><td> #CACAFF</td></tr>
    <tr bgcolor="#BCBCEE"><td>DarkOliveGreen2 </td><td>188 </td><td>238 </td><td>104</td><td> #BCBCEE</td></tr>
    <tr bgcolor="#A2A2CD"><td>DarkOliveGreen3 </td><td>162 </td><td>205 </td><td>90</td><td> #A2A2CD</td></tr>
    <tr bgcolor="#6E6E8B"><td>DarkOliveGreen4 </td><td>110 </td><td>139 </td><td>61</td><td> #6E6E8B</td></tr>
    <tr bgcolor="#FFFF8C"><td>DarkOrange </td><td>255 </td><td>140 </td><td>0</td><td> #FFFF8C</td></tr>
    <tr bgcolor="#FFFF7F"><td>DarkOrange1 </td><td>255 </td><td>127 </td><td>0</td><td> #FFFF7F</td></tr>
    <tr bgcolor="#EEEE76"><td>DarkOrange2 </td><td>238 </td><td>118 </td><td>0</td><td> #EEEE76</td></tr>
    <tr bgcolor="#CDCD66"><td>DarkOrange3 </td><td>205 </td><td>102 </td><td>0</td><td> #CDCD66</td></tr>
    <tr bgcolor="#8B8B45"><td>DarkOrange4 </td><td>139 </td><td>69 </td><td>0</td><td> #8B8B45</td></tr>
    <tr bgcolor="#999932"><td>DarkOrchid </td><td>153 </td><td>50 </td><td>204</td><td> #999932</td></tr>
    <tr bgcolor="#BFBF3E"><td>DarkOrchid1 </td><td>191 </td><td>62 </td><td>255</td><td> #BFBF3E</td></tr>
    <tr bgcolor="#B2B23A"><td>DarkOrchid2 </td><td>178 </td><td>58 </td><td>238</td><td> #B2B23A</td></tr>
    <tr bgcolor="#9A9A32"><td>DarkOrchid3 </td><td>154 </td><td>50 </td><td>205</td><td> #9A9A32</td></tr>
    <tr bgcolor="#686822"><td>DarkOrchid4 </td><td>104 </td><td>34 </td><td>139</td><td> #686822</td></tr>
    <tr bgcolor="#8B8B00"><td>DarkRed </td><td>139 </td><td>0 </td><td>0</td><td> #8B8B00</td></tr>
    <tr bgcolor="#E9E996"><td>DarkSalmon </td><td>233 </td><td>150 </td><td>122</td><td> #E9E996</td></tr>
    <tr bgcolor="#8F8FBC"><td>DarkSeaGreen </td><td>143 </td><td>188 </td><td>143</td><td> #8F8FBC</td></tr>
    <tr bgcolor="#C1C1FF"><td>DarkSeaGreen1 </td><td>193 </td><td>255 </td><td>193</td><td> #C1C1FF</td></tr>
    <tr bgcolor="#B4B4EE"><td>DarkSeaGreen2 </td><td>180 </td><td>238 </td><td>180</td><td> #B4B4EE</td></tr>
    <tr bgcolor="#9B9BCD"><td>DarkSeaGreen3 </td><td>155 </td><td>205 </td><td>155</td><td> #9B9BCD</td></tr>
    <tr bgcolor="#69698B"><td>DarkSeaGreen4 </td><td>105 </td><td>139 </td><td>105</td><td> #69698B</td></tr>
    <tr bgcolor="#48483D"><td>DarkSlateBlue </td><td>72 </td><td>61 </td><td>139</td><td> #48483D</td></tr>
    <tr bgcolor="#2F2F4F"><td>DarkSlateGray </td><td>47 </td><td>79 </td><td>79</td><td> #2F2F4F</td></tr>
    <tr bgcolor="#9797FF"><td>DarkSlateGray1 </td><td>151 </td><td>255 </td><td>255</td><td> #9797FF</td></tr>
    <tr bgcolor="#8D8DEE"><td>DarkSlateGray2 </td><td>141 </td><td>238 </td><td>238</td><td> #8D8DEE</td></tr>
    <tr bgcolor="#7979CD"><td>DarkSlateGray3 </td><td>121 </td><td>205 </td><td>205</td><td> #7979CD</td></tr>
    <tr bgcolor="#52528B"><td>DarkSlateGray4 </td><td>82 </td><td>139 </td><td>139</td><td> #52528B</td></tr>
    <tr bgcolor="#2F2F4F"><td>DarkSlateGrey </td><td>47 </td><td>79 </td><td>79</td><td> #2F2F4F</td></tr>
    <tr bgcolor="#0000CE"><td>DarkTurquoise </td><td>0 </td><td>206 </td><td>209</td><td> #0000CE</td></tr>
    <tr bgcolor="#949400"><td>DarkViolet </td><td>148 </td><td>0 </td><td>211</td><td> #949400</td></tr>
    <tr bgcolor="#FFFF14"><td>deep pink </td><td>255 </td><td>20 </td><td>147</td><td> #FFFF14</td></tr>
    <tr bgcolor="#0000BF"><td>deep sky blue </td><td>0 </td><td>191 </td><td>255</td><td> #0000BF</td></tr>
    <tr bgcolor="#FFFF14"><td>DeepPink </td><td>255 </td><td>20 </td><td>147</td><td> #FFFF14</td></tr>
    <tr bgcolor="#FFFF14"><td>DeepPink1 </td><td>255 </td><td>20 </td><td>147</td><td> #FFFF14</td></tr>
    <tr bgcolor="#EEEE12"><td>DeepPink2 </td><td>238 </td><td>18 </td><td>137</td><td> #EEEE12</td></tr>
    <tr bgcolor="#CDCD10"><td>DeepPink3 </td><td>205 </td><td>16 </td><td>118</td><td> #CDCD10</td></tr>
    <tr bgcolor="#8B8B0A"><td>DeepPink4 </td><td>139 </td><td>10 </td><td>80</td><td> #8B8B0A</td></tr>
    <tr bgcolor="#0000BF"><td>DeepSkyBlue </td><td>0 </td><td>191 </td><td>255</td><td> #0000BF</td></tr>
    <tr bgcolor="#0000BF"><td>DeepSkyBlue1 </td><td>0 </td><td>191 </td><td>255</td><td> #0000BF</td></tr>
    <tr bgcolor="#0000B2"><td>DeepSkyBlue2 </td><td>0 </td><td>178 </td><td>238</td><td> #0000B2</td></tr>
    <tr bgcolor="#00009A"><td>DeepSkyBlue3 </td><td>0 </td><td>154 </td><td>205</td><td> #00009A</td></tr>
    <tr bgcolor="#000068"><td>DeepSkyBlue4 </td><td>0 </td><td>104 </td><td>139</td><td> #000068</td></tr>
    <tr bgcolor="#696969"><td>dim gray </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#696969"><td>dim grey </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#696969"><td>DimGray </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#696969"><td>DimGrey </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#1E1E90"><td>dodger blue </td><td>30 </td><td>144 </td><td>255</td><td> #1E1E90</td></tr>
    <tr bgcolor="#1E1E90"><td>DodgerBlue </td><td>30 </td><td>144 </td><td>255</td><td> #1E1E90</td></tr>
    <tr bgcolor="#1E1E90"><td>DodgerBlue1 </td><td>30 </td><td>144 </td><td>255</td><td> #1E1E90</td></tr>
    <tr bgcolor="#1C1C86"><td>DodgerBlue2 </td><td>28 </td><td>134 </td><td>238</td><td> #1C1C86</td></tr>
    <tr bgcolor="#181874"><td>DodgerBlue3 </td><td>24 </td><td>116 </td><td>205</td><td> #181874</td></tr>
    <tr bgcolor="#10104E"><td>DodgerBlue4 </td><td>16 </td><td>78 </td><td>139</td><td> #10104E</td></tr>
    <tr bgcolor="#B2B222"><td>firebrick </td><td>178 </td><td>34 </td><td>34</td><td> #B2B222</td></tr>
    <tr bgcolor="#FFFF30"><td>firebrick1 </td><td>255 </td><td>48 </td><td>48</td><td> #FFFF30</td></tr>
    <tr bgcolor="#EEEE2C"><td>firebrick2 </td><td>238 </td><td>44 </td><td>44</td><td> #EEEE2C</td></tr>
    <tr bgcolor="#CDCD26"><td>firebrick3 </td><td>205 </td><td>38 </td><td>38</td><td> #CDCD26</td></tr>
    <tr bgcolor="#8B8B1A"><td>firebrick4 </td><td>139 </td><td>26 </td><td>26</td><td> #8B8B1A</td></tr>
    <tr bgcolor="#FFFFFA"><td>floral white </td><td>255 </td><td>250 </td><td>240</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#FFFFFA"><td>FloralWhite </td><td>255 </td><td>250 </td><td>240</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#22228B"><td>forest green </td><td>34 </td><td>139 </td><td>34</td><td> #22228B</td></tr>
    <tr bgcolor="#22228B"><td>ForestGreen </td><td>34 </td><td>139 </td><td>34</td><td> #22228B</td></tr>
    <tr bgcolor="#FFFF00"><td>fuchsia </td><td>255 </td><td>0 </td><td>255</td><td> #FFFF00</td></tr>
    <tr bgcolor="#DCDCDC"><td>gainsboro </td><td>220 </td><td>220 </td><td>220</td><td> #DCDCDC</td></tr>
    <tr bgcolor="#F8F8F8"><td>ghost white </td><td>248 </td><td>248 </td><td>255</td><td> #F8F8F8</td></tr>
    <tr bgcolor="#F8F8F8"><td>GhostWhite </td><td>248 </td><td>248 </td><td>255</td><td> #F8F8F8</td></tr>
    <tr bgcolor="#FFFFD7"><td>gold </td><td>255 </td><td>215 </td><td>0</td><td> #FFFFD7</td></tr>
    <tr bgcolor="#FFFFD7"><td>gold1 </td><td>255 </td><td>215 </td><td>0</td><td> #FFFFD7</td></tr>
    <tr bgcolor="#EEEEC9"><td>gold2 </td><td>238 </td><td>201 </td><td>0</td><td> #EEEEC9</td></tr>
    <tr bgcolor="#CDCDAD"><td>gold3 </td><td>205 </td><td>173 </td><td>0</td><td> #CDCDAD</td></tr>
    <tr bgcolor="#8B8B75"><td>gold4 </td><td>139 </td><td>117 </td><td>0</td><td> #8B8B75</td></tr>
    <tr bgcolor="#DADAA5"><td>goldenrod </td><td>218 </td><td>165 </td><td>32</td><td> #DADAA5</td></tr>
    <tr bgcolor="#FFFFC1"><td>goldenrod1 </td><td>255 </td><td>193 </td><td>37</td><td> #FFFFC1</td></tr>
    <tr bgcolor="#EEEEB4"><td>goldenrod2 </td><td>238 </td><td>180 </td><td>34</td><td> #EEEEB4</td></tr>
    <tr bgcolor="#CDCD9B"><td>goldenrod3 </td><td>205 </td><td>155 </td><td>29</td><td> #CDCD9B</td></tr>
    <tr bgcolor="#8B8B69"><td>goldenrod4 </td><td>139 </td><td>105 </td><td>20</td><td> #8B8B69</td></tr>
    <tr bgcolor="#808080"><td>gray </td><td>128 </td><td>128 </td><td>128</td><td> #808080</td></tr>
    <tr bgcolor="#000000"><td>gray0 </td><td>0 </td><td>0 </td><td>0</td><td> #000000</td></tr>
    <tr bgcolor="#030303"><td>gray1 </td><td>3 </td><td>3 </td><td>3</td><td> #030303</td></tr>
    <tr bgcolor="#050505"><td>gray2 </td><td>5 </td><td>5 </td><td>5</td><td> #050505</td></tr>
    <tr bgcolor="#080808"><td>gray3 </td><td>8 </td><td>8 </td><td>8</td><td> #080808</td></tr>
    <tr bgcolor="#0A0A0A"><td>gray4 </td><td>10 </td><td>10 </td><td>10</td><td> #0A0A0A</td></tr>
    <tr bgcolor="#0D0D0D"><td>gray5 </td><td>13 </td><td>13 </td><td>13</td><td> #0D0D0D</td></tr>
    <tr bgcolor="#0F0F0F"><td>gray6 </td><td>15 </td><td>15 </td><td>15</td><td> #0F0F0F</td></tr>
    <tr bgcolor="#121212"><td>gray7 </td><td>18 </td><td>18 </td><td>18</td><td> #121212</td></tr>
    <tr bgcolor="#141414"><td>gray8 </td><td>20 </td><td>20 </td><td>20</td><td> #141414</td></tr>
    <tr bgcolor="#171717"><td>gray9 </td><td>23 </td><td>23 </td><td>23</td><td> #171717</td></tr>
    <tr bgcolor="#1A1A1A"><td>gray10 </td><td>26 </td><td>26 </td><td>26</td><td> #1A1A1A</td></tr>
    <tr bgcolor="#1C1C1C"><td>gray11 </td><td>28 </td><td>28 </td><td>28</td><td> #1C1C1C</td></tr>
    <tr bgcolor="#1F1F1F"><td>gray12 </td><td>31 </td><td>31 </td><td>31</td><td> #1F1F1F</td></tr>
    <tr bgcolor="#212121"><td>gray13 </td><td>33 </td><td>33 </td><td>33</td><td> #212121</td></tr>
    <tr bgcolor="#242424"><td>gray14 </td><td>36 </td><td>36 </td><td>36</td><td> #242424</td></tr>
    <tr bgcolor="#262626"><td>gray15 </td><td>38 </td><td>38 </td><td>38</td><td> #262626</td></tr>
    <tr bgcolor="#292929"><td>gray16 </td><td>41 </td><td>41 </td><td>41</td><td> #292929</td></tr>
    <tr bgcolor="#2B2B2B"><td>gray17 </td><td>43 </td><td>43 </td><td>43</td><td> #2B2B2B</td></tr>
    <tr bgcolor="#2E2E2E"><td>gray18 </td><td>46 </td><td>46 </td><td>46</td><td> #2E2E2E</td></tr>
    <tr bgcolor="#303030"><td>gray19 </td><td>48 </td><td>48 </td><td>48</td><td> #303030</td></tr>
    <tr bgcolor="#333333"><td>gray20 </td><td>51 </td><td>51 </td><td>51</td><td> #333333</td></tr>
    <tr bgcolor="#363636"><td>gray21 </td><td>54 </td><td>54 </td><td>54</td><td> #363636</td></tr>
    <tr bgcolor="#383838"><td>gray22 </td><td>56 </td><td>56 </td><td>56</td><td> #383838</td></tr>
    <tr bgcolor="#3B3B3B"><td>gray23 </td><td>59 </td><td>59 </td><td>59</td><td> #3B3B3B</td></tr>
    <tr bgcolor="#3D3D3D"><td>gray24 </td><td>61 </td><td>61 </td><td>61</td><td> #3D3D3D</td></tr>
    <tr bgcolor="#404040"><td>gray25 </td><td>64 </td><td>64 </td><td>64</td><td> #404040</td></tr>
    <tr bgcolor="#424242"><td>gray26 </td><td>66 </td><td>66 </td><td>66</td><td> #424242</td></tr>
    <tr bgcolor="#454545"><td>gray27 </td><td>69 </td><td>69 </td><td>69</td><td> #454545</td></tr>
    <tr bgcolor="#474747"><td>gray28 </td><td>71 </td><td>71 </td><td>71</td><td> #474747</td></tr>
    <tr bgcolor="#4A4A4A"><td>gray29 </td><td>74 </td><td>74 </td><td>74</td><td> #4A4A4A</td></tr>
    <tr bgcolor="#4D4D4D"><td>gray30 </td><td>77 </td><td>77 </td><td>77</td><td> #4D4D4D</td></tr>
    <tr bgcolor="#4F4F4F"><td>gray31 </td><td>79 </td><td>79 </td><td>79</td><td> #4F4F4F</td></tr>
    <tr bgcolor="#525252"><td>gray32 </td><td>82 </td><td>82 </td><td>82</td><td> #525252</td></tr>
    <tr bgcolor="#545454"><td>gray33 </td><td>84 </td><td>84 </td><td>84</td><td> #545454</td></tr>
    <tr bgcolor="#575757"><td>gray34 </td><td>87 </td><td>87 </td><td>87</td><td> #575757</td></tr>
    <tr bgcolor="#595959"><td>gray35 </td><td>89 </td><td>89 </td><td>89</td><td> #595959</td></tr>
    <tr bgcolor="#5C5C5C"><td>gray36 </td><td>92 </td><td>92 </td><td>92</td><td> #5C5C5C</td></tr>
    <tr bgcolor="#5E5E5E"><td>gray37 </td><td>94 </td><td>94 </td><td>94</td><td> #5E5E5E</td></tr>
    <tr bgcolor="#616161"><td>gray38 </td><td>97 </td><td>97 </td><td>97</td><td> #616161</td></tr>
    <tr bgcolor="#636363"><td>gray39 </td><td>99 </td><td>99 </td><td>99</td><td> #636363</td></tr>
    <tr bgcolor="#666666"><td>gray40 </td><td>102 </td><td>102 </td><td>102</td><td> #666666</td></tr>
    <tr bgcolor="#696969"><td>gray41 </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#6B6B6B"><td>gray42 </td><td>107 </td><td>107 </td><td>107</td><td> #6B6B6B</td></tr>
    <tr bgcolor="#6E6E6E"><td>gray43 </td><td>110 </td><td>110 </td><td>110</td><td> #6E6E6E</td></tr>
    <tr bgcolor="#707070"><td>gray44 </td><td>112 </td><td>112 </td><td>112</td><td> #707070</td></tr>
    <tr bgcolor="#737373"><td>gray45 </td><td>115 </td><td>115 </td><td>115</td><td> #737373</td></tr>
    <tr bgcolor="#757575"><td>gray46 </td><td>117 </td><td>117 </td><td>117</td><td> #757575</td></tr>
    <tr bgcolor="#787878"><td>gray47 </td><td>120 </td><td>120 </td><td>120</td><td> #787878</td></tr>
    <tr bgcolor="#7A7A7A"><td>gray48 </td><td>122 </td><td>122 </td><td>122</td><td> #7A7A7A</td></tr>
    <tr bgcolor="#7D7D7D"><td>gray49 </td><td>125 </td><td>125 </td><td>125</td><td> #7D7D7D</td></tr>
    <tr bgcolor="#7F7F7F"><td>gray50 </td><td>127 </td><td>127 </td><td>127</td><td> #7F7F7F</td></tr>
    <tr bgcolor="#828282"><td>gray51 </td><td>130 </td><td>130 </td><td>130</td><td> #828282</td></tr>
    <tr bgcolor="#858585"><td>gray52 </td><td>133 </td><td>133 </td><td>133</td><td> #858585</td></tr>
    <tr bgcolor="#878787"><td>gray53 </td><td>135 </td><td>135 </td><td>135</td><td> #878787</td></tr>
    <tr bgcolor="#8A8A8A"><td>gray54 </td><td>138 </td><td>138 </td><td>138</td><td> #8A8A8A</td></tr>
    <tr bgcolor="#8C8C8C"><td>gray55 </td><td>140 </td><td>140 </td><td>140</td><td> #8C8C8C</td></tr>
    <tr bgcolor="#8F8F8F"><td>gray56 </td><td>143 </td><td>143 </td><td>143</td><td> #8F8F8F</td></tr>
    <tr bgcolor="#919191"><td>gray57 </td><td>145 </td><td>145 </td><td>145</td><td> #919191</td></tr>
    <tr bgcolor="#949494"><td>gray58 </td><td>148 </td><td>148 </td><td>148</td><td> #949494</td></tr>
    <tr bgcolor="#969696"><td>gray59 </td><td>150 </td><td>150 </td><td>150</td><td> #969696</td></tr>
    <tr bgcolor="#999999"><td>gray60 </td><td>153 </td><td>153 </td><td>153</td><td> #999999</td></tr>
    <tr bgcolor="#9C9C9C"><td>gray61 </td><td>156 </td><td>156 </td><td>156</td><td> #9C9C9C</td></tr>
    <tr bgcolor="#9E9E9E"><td>gray62 </td><td>158 </td><td>158 </td><td>158</td><td> #9E9E9E</td></tr>
    <tr bgcolor="#A1A1A1"><td>gray63 </td><td>161 </td><td>161 </td><td>161</td><td> #A1A1A1</td></tr>
    <tr bgcolor="#A3A3A3"><td>gray64 </td><td>163 </td><td>163 </td><td>163</td><td> #A3A3A3</td></tr>
    <tr bgcolor="#A6A6A6"><td>gray65 </td><td>166 </td><td>166 </td><td>166</td><td> #A6A6A6</td></tr>
    <tr bgcolor="#A8A8A8"><td>gray66 </td><td>168 </td><td>168 </td><td>168</td><td> #A8A8A8</td></tr>
    <tr bgcolor="#ABABAB"><td>gray67 </td><td>171 </td><td>171 </td><td>171</td><td> #ABABAB</td></tr>
    <tr bgcolor="#ADADAD"><td>gray68 </td><td>173 </td><td>173 </td><td>173</td><td> #ADADAD</td></tr>
    <tr bgcolor="#B0B0B0"><td>gray69 </td><td>176 </td><td>176 </td><td>176</td><td> #B0B0B0</td></tr>
    <tr bgcolor="#B3B3B3"><td>gray70 </td><td>179 </td><td>179 </td><td>179</td><td> #B3B3B3</td></tr>
    <tr bgcolor="#B5B5B5"><td>gray71 </td><td>181 </td><td>181 </td><td>181</td><td> #B5B5B5</td></tr>
    <tr bgcolor="#B8B8B8"><td>gray72 </td><td>184 </td><td>184 </td><td>184</td><td> #B8B8B8</td></tr>
    <tr bgcolor="#BABABA"><td>gray73 </td><td>186 </td><td>186 </td><td>186</td><td> #BABABA</td></tr>
    <tr bgcolor="#BDBDBD"><td>gray74 </td><td>189 </td><td>189 </td><td>189</td><td> #BDBDBD</td></tr>
    <tr bgcolor="#BFBFBF"><td>gray75 </td><td>191 </td><td>191 </td><td>191</td><td> #BFBFBF</td></tr>
    <tr bgcolor="#C2C2C2"><td>gray76 </td><td>194 </td><td>194 </td><td>194</td><td> #C2C2C2</td></tr>
    <tr bgcolor="#C4C4C4"><td>gray77 </td><td>196 </td><td>196 </td><td>196</td><td> #C4C4C4</td></tr>
    <tr bgcolor="#C7C7C7"><td>gray78 </td><td>199 </td><td>199 </td><td>199</td><td> #C7C7C7</td></tr>
    <tr bgcolor="#C9C9C9"><td>gray79 </td><td>201 </td><td>201 </td><td>201</td><td> #C9C9C9</td></tr>
    <tr bgcolor="#CCCCCC"><td>gray80 </td><td>204 </td><td>204 </td><td>204</td><td> #CCCCCC</td></tr>
    <tr bgcolor="#CFCFCF"><td>gray81 </td><td>207 </td><td>207 </td><td>207</td><td> #CFCFCF</td></tr>
    <tr bgcolor="#D1D1D1"><td>gray82 </td><td>209 </td><td>209 </td><td>209</td><td> #D1D1D1</td></tr>
    <tr bgcolor="#D4D4D4"><td>gray83 </td><td>212 </td><td>212 </td><td>212</td><td> #D4D4D4</td></tr>
    <tr bgcolor="#D6D6D6"><td>gray84 </td><td>214 </td><td>214 </td><td>214</td><td> #D6D6D6</td></tr>
    <tr bgcolor="#D9D9D9"><td>gray85 </td><td>217 </td><td>217 </td><td>217</td><td> #D9D9D9</td></tr>
    <tr bgcolor="#DBDBDB"><td>gray86 </td><td>219 </td><td>219 </td><td>219</td><td> #DBDBDB</td></tr>
    <tr bgcolor="#DEDEDE"><td>gray87 </td><td>222 </td><td>222 </td><td>222</td><td> #DEDEDE</td></tr>
    <tr bgcolor="#E0E0E0"><td>gray88 </td><td>224 </td><td>224 </td><td>224</td><td> #E0E0E0</td></tr>
    <tr bgcolor="#E3E3E3"><td>gray89 </td><td>227 </td><td>227 </td><td>227</td><td> #E3E3E3</td></tr>
    <tr bgcolor="#E5E5E5"><td>gray90 </td><td>229 </td><td>229 </td><td>229</td><td> #E5E5E5</td></tr>
    <tr bgcolor="#E8E8E8"><td>gray91 </td><td>232 </td><td>232 </td><td>232</td><td> #E8E8E8</td></tr>
    <tr bgcolor="#EBEBEB"><td>gray92 </td><td>235 </td><td>235 </td><td>235</td><td> #EBEBEB</td></tr>
    <tr bgcolor="#EDEDED"><td>gray93 </td><td>237 </td><td>237 </td><td>237</td><td> #EDEDED</td></tr>
    <tr bgcolor="#F0F0F0"><td>gray94 </td><td>240 </td><td>240 </td><td>240</td><td> #F0F0F0</td></tr>
    <tr bgcolor="#F2F2F2"><td>gray95 </td><td>242 </td><td>242 </td><td>242</td><td> #F2F2F2</td></tr>
    <tr bgcolor="#F5F5F5"><td>gray96 </td><td>245 </td><td>245 </td><td>245</td><td> #F5F5F5</td></tr>
    <tr bgcolor="#F7F7F7"><td>gray97 </td><td>247 </td><td>247 </td><td>247</td><td> #F7F7F7</td></tr>
    <tr bgcolor="#FAFAFA"><td>gray98 </td><td>250 </td><td>250 </td><td>250</td><td> #FAFAFA</td></tr>
    <tr bgcolor="#FCFCFC"><td>gray99 </td><td>252 </td><td>252 </td><td>252</td><td> #FCFCFC</td></tr>
    <tr bgcolor="#FFFFFF"><td>gray100 </td><td>255 </td><td>255 </td><td>255</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#000080"><td>green </td><td>0 </td><td>128 </td><td>0</td><td> #000080</td></tr>
    <tr bgcolor="#ADADFF"><td>green yellow </td><td>173 </td><td>255 </td><td>47</td><td> #ADADFF</td></tr>
    <tr bgcolor="#0000FF"><td>green1 </td><td>0 </td><td>255 </td><td>0</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000EE"><td>green2 </td><td>0 </td><td>238 </td><td>0</td><td> #0000EE</td></tr>
    <tr bgcolor="#0000CD"><td>green3 </td><td>0 </td><td>205 </td><td>0</td><td> #0000CD</td></tr>
    <tr bgcolor="#00008B"><td>green4 </td><td>0 </td><td>139 </td><td>0</td><td> #00008B</td></tr>
    <tr bgcolor="#ADADFF"><td>GreenYellow </td><td>173 </td><td>255 </td><td>47</td><td> #ADADFF</td></tr>
    <tr bgcolor="#808080"><td>grey </td><td>128 </td><td>128 </td><td>128</td><td> #808080</td></tr>
    <tr bgcolor="#000000"><td>grey0 </td><td>0 </td><td>0 </td><td>0</td><td> #000000</td></tr>
    <tr bgcolor="#030303"><td>grey1 </td><td>3 </td><td>3 </td><td>3</td><td> #030303</td></tr>
    <tr bgcolor="#050505"><td>grey2 </td><td>5 </td><td>5 </td><td>5</td><td> #050505</td></tr>
    <tr bgcolor="#080808"><td>grey3 </td><td>8 </td><td>8 </td><td>8</td><td> #080808</td></tr>
    <tr bgcolor="#0A0A0A"><td>grey4 </td><td>10 </td><td>10 </td><td>10</td><td> #0A0A0A</td></tr>
    <tr bgcolor="#0D0D0D"><td>grey5 </td><td>13 </td><td>13 </td><td>13</td><td> #0D0D0D</td></tr>
    <tr bgcolor="#0F0F0F"><td>grey6 </td><td>15 </td><td>15 </td><td>15</td><td> #0F0F0F</td></tr>
    <tr bgcolor="#121212"><td>grey7 </td><td>18 </td><td>18 </td><td>18</td><td> #121212</td></tr>
    <tr bgcolor="#141414"><td>grey8 </td><td>20 </td><td>20 </td><td>20</td><td> #141414</td></tr>
    <tr bgcolor="#171717"><td>grey9 </td><td>23 </td><td>23 </td><td>23</td><td> #171717</td></tr>
    <tr bgcolor="#1A1A1A"><td>grey10 </td><td>26 </td><td>26 </td><td>26</td><td> #1A1A1A</td></tr>
    <tr bgcolor="#1C1C1C"><td>grey11 </td><td>28 </td><td>28 </td><td>28</td><td> #1C1C1C</td></tr>
    <tr bgcolor="#1F1F1F"><td>grey12 </td><td>31 </td><td>31 </td><td>31</td><td> #1F1F1F</td></tr>
    <tr bgcolor="#212121"><td>grey13 </td><td>33 </td><td>33 </td><td>33</td><td> #212121</td></tr>
    <tr bgcolor="#242424"><td>grey14 </td><td>36 </td><td>36 </td><td>36</td><td> #242424</td></tr>
    <tr bgcolor="#262626"><td>grey15 </td><td>38 </td><td>38 </td><td>38</td><td> #262626</td></tr>
    <tr bgcolor="#292929"><td>grey16 </td><td>41 </td><td>41 </td><td>41</td><td> #292929</td></tr>
    <tr bgcolor="#2B2B2B"><td>grey17 </td><td>43 </td><td>43 </td><td>43</td><td> #2B2B2B</td></tr>
    <tr bgcolor="#2E2E2E"><td>grey18 </td><td>46 </td><td>46 </td><td>46</td><td> #2E2E2E</td></tr>
    <tr bgcolor="#303030"><td>grey19 </td><td>48 </td><td>48 </td><td>48</td><td> #303030</td></tr>
    <tr bgcolor="#333333"><td>grey20 </td><td>51 </td><td>51 </td><td>51</td><td> #333333</td></tr>
    <tr bgcolor="#363636"><td>grey21 </td><td>54 </td><td>54 </td><td>54</td><td> #363636</td></tr>
    <tr bgcolor="#383838"><td>grey22 </td><td>56 </td><td>56 </td><td>56</td><td> #383838</td></tr>
    <tr bgcolor="#3B3B3B"><td>grey23 </td><td>59 </td><td>59 </td><td>59</td><td> #3B3B3B</td></tr>
    <tr bgcolor="#3D3D3D"><td>grey24 </td><td>61 </td><td>61 </td><td>61</td><td> #3D3D3D</td></tr>
    <tr bgcolor="#404040"><td>grey25 </td><td>64 </td><td>64 </td><td>64</td><td> #404040</td></tr>
    <tr bgcolor="#424242"><td>grey26 </td><td>66 </td><td>66 </td><td>66</td><td> #424242</td></tr>
    <tr bgcolor="#454545"><td>grey27 </td><td>69 </td><td>69 </td><td>69</td><td> #454545</td></tr>
    <tr bgcolor="#474747"><td>grey28 </td><td>71 </td><td>71 </td><td>71</td><td> #474747</td></tr>
    <tr bgcolor="#4A4A4A"><td>grey29 </td><td>74 </td><td>74 </td><td>74</td><td> #4A4A4A</td></tr>
    <tr bgcolor="#4D4D4D"><td>grey30 </td><td>77 </td><td>77 </td><td>77</td><td> #4D4D4D</td></tr>
    <tr bgcolor="#4F4F4F"><td>grey31 </td><td>79 </td><td>79 </td><td>79</td><td> #4F4F4F</td></tr>
    <tr bgcolor="#525252"><td>grey32 </td><td>82 </td><td>82 </td><td>82</td><td> #525252</td></tr>
    <tr bgcolor="#545454"><td>grey33 </td><td>84 </td><td>84 </td><td>84</td><td> #545454</td></tr>
    <tr bgcolor="#575757"><td>grey34 </td><td>87 </td><td>87 </td><td>87</td><td> #575757</td></tr>
    <tr bgcolor="#595959"><td>grey35 </td><td>89 </td><td>89 </td><td>89</td><td> #595959</td></tr>
    <tr bgcolor="#5C5C5C"><td>grey36 </td><td>92 </td><td>92 </td><td>92</td><td> #5C5C5C</td></tr>
    <tr bgcolor="#5E5E5E"><td>grey37 </td><td>94 </td><td>94 </td><td>94</td><td> #5E5E5E</td></tr>
    <tr bgcolor="#616161"><td>grey38 </td><td>97 </td><td>97 </td><td>97</td><td> #616161</td></tr>
    <tr bgcolor="#636363"><td>grey39 </td><td>99 </td><td>99 </td><td>99</td><td> #636363</td></tr>
    <tr bgcolor="#666666"><td>grey40 </td><td>102 </td><td>102 </td><td>102</td><td> #666666</td></tr>
    <tr bgcolor="#696969"><td>grey41 </td><td>105 </td><td>105 </td><td>105</td><td> #696969</td></tr>
    <tr bgcolor="#6B6B6B"><td>grey42 </td><td>107 </td><td>107 </td><td>107</td><td> #6B6B6B</td></tr>
    <tr bgcolor="#6E6E6E"><td>grey43 </td><td>110 </td><td>110 </td><td>110</td><td> #6E6E6E</td></tr>
    <tr bgcolor="#707070"><td>grey44 </td><td>112 </td><td>112 </td><td>112</td><td> #707070</td></tr>
    <tr bgcolor="#737373"><td>grey45 </td><td>115 </td><td>115 </td><td>115</td><td> #737373</td></tr>
    <tr bgcolor="#757575"><td>grey46 </td><td>117 </td><td>117 </td><td>117</td><td> #757575</td></tr>
    <tr bgcolor="#787878"><td>grey47 </td><td>120 </td><td>120 </td><td>120</td><td> #787878</td></tr>
    <tr bgcolor="#7A7A7A"><td>grey48 </td><td>122 </td><td>122 </td><td>122</td><td> #7A7A7A</td></tr>
    <tr bgcolor="#7D7D7D"><td>grey49 </td><td>125 </td><td>125 </td><td>125</td><td> #7D7D7D</td></tr>
    <tr bgcolor="#7F7F7F"><td>grey50 </td><td>127 </td><td>127 </td><td>127</td><td> #7F7F7F</td></tr>
    <tr bgcolor="#828282"><td>grey51 </td><td>130 </td><td>130 </td><td>130</td><td> #828282</td></tr>
    <tr bgcolor="#858585"><td>grey52 </td><td>133 </td><td>133 </td><td>133</td><td> #858585</td></tr>
    <tr bgcolor="#878787"><td>grey53 </td><td>135 </td><td>135 </td><td>135</td><td> #878787</td></tr>
    <tr bgcolor="#8A8A8A"><td>grey54 </td><td>138 </td><td>138 </td><td>138</td><td> #8A8A8A</td></tr>
    <tr bgcolor="#8C8C8C"><td>grey55 </td><td>140 </td><td>140 </td><td>140</td><td> #8C8C8C</td></tr>
    <tr bgcolor="#8F8F8F"><td>grey56 </td><td>143 </td><td>143 </td><td>143</td><td> #8F8F8F</td></tr>
    <tr bgcolor="#919191"><td>grey57 </td><td>145 </td><td>145 </td><td>145</td><td> #919191</td></tr>
    <tr bgcolor="#949494"><td>grey58 </td><td>148 </td><td>148 </td><td>148</td><td> #949494</td></tr>
    <tr bgcolor="#969696"><td>grey59 </td><td>150 </td><td>150 </td><td>150</td><td> #969696</td></tr>
    <tr bgcolor="#999999"><td>grey60 </td><td>153 </td><td>153 </td><td>153</td><td> #999999</td></tr>
    <tr bgcolor="#9C9C9C"><td>grey61 </td><td>156 </td><td>156 </td><td>156</td><td> #9C9C9C</td></tr>
    <tr bgcolor="#9E9E9E"><td>grey62 </td><td>158 </td><td>158 </td><td>158</td><td> #9E9E9E</td></tr>
    <tr bgcolor="#A1A1A1"><td>grey63 </td><td>161 </td><td>161 </td><td>161</td><td> #A1A1A1</td></tr>
    <tr bgcolor="#A3A3A3"><td>grey64 </td><td>163 </td><td>163 </td><td>163</td><td> #A3A3A3</td></tr>
    <tr bgcolor="#A6A6A6"><td>grey65 </td><td>166 </td><td>166 </td><td>166</td><td> #A6A6A6</td></tr>
    <tr bgcolor="#A8A8A8"><td>grey66 </td><td>168 </td><td>168 </td><td>168</td><td> #A8A8A8</td></tr>
    <tr bgcolor="#ABABAB"><td>grey67 </td><td>171 </td><td>171 </td><td>171</td><td> #ABABAB</td></tr>
    <tr bgcolor="#ADADAD"><td>grey68 </td><td>173 </td><td>173 </td><td>173</td><td> #ADADAD</td></tr>
    <tr bgcolor="#B0B0B0"><td>grey69 </td><td>176 </td><td>176 </td><td>176</td><td> #B0B0B0</td></tr>
    <tr bgcolor="#B3B3B3"><td>grey70 </td><td>179 </td><td>179 </td><td>179</td><td> #B3B3B3</td></tr>
    <tr bgcolor="#B5B5B5"><td>grey71 </td><td>181 </td><td>181 </td><td>181</td><td> #B5B5B5</td></tr>
    <tr bgcolor="#B8B8B8"><td>grey72 </td><td>184 </td><td>184 </td><td>184</td><td> #B8B8B8</td></tr>
    <tr bgcolor="#BABABA"><td>grey73 </td><td>186 </td><td>186 </td><td>186</td><td> #BABABA</td></tr>
    <tr bgcolor="#BDBDBD"><td>grey74 </td><td>189 </td><td>189 </td><td>189</td><td> #BDBDBD</td></tr>
    <tr bgcolor="#BFBFBF"><td>grey75 </td><td>191 </td><td>191 </td><td>191</td><td> #BFBFBF</td></tr>
    <tr bgcolor="#C2C2C2"><td>grey76 </td><td>194 </td><td>194 </td><td>194</td><td> #C2C2C2</td></tr>
    <tr bgcolor="#C4C4C4"><td>grey77 </td><td>196 </td><td>196 </td><td>196</td><td> #C4C4C4</td></tr>
    <tr bgcolor="#C7C7C7"><td>grey78 </td><td>199 </td><td>199 </td><td>199</td><td> #C7C7C7</td></tr>
    <tr bgcolor="#C9C9C9"><td>grey79 </td><td>201 </td><td>201 </td><td>201</td><td> #C9C9C9</td></tr>
    <tr bgcolor="#CCCCCC"><td>grey80 </td><td>204 </td><td>204 </td><td>204</td><td> #CCCCCC</td></tr>
    <tr bgcolor="#CFCFCF"><td>grey81 </td><td>207 </td><td>207 </td><td>207</td><td> #CFCFCF</td></tr>
    <tr bgcolor="#D1D1D1"><td>grey82 </td><td>209 </td><td>209 </td><td>209</td><td> #D1D1D1</td></tr>
    <tr bgcolor="#D4D4D4"><td>grey83 </td><td>212 </td><td>212 </td><td>212</td><td> #D4D4D4</td></tr>
    <tr bgcolor="#D6D6D6"><td>grey84 </td><td>214 </td><td>214 </td><td>214</td><td> #D6D6D6</td></tr>
    <tr bgcolor="#D9D9D9"><td>grey85 </td><td>217 </td><td>217 </td><td>217</td><td> #D9D9D9</td></tr>
    <tr bgcolor="#DBDBDB"><td>grey86 </td><td>219 </td><td>219 </td><td>219</td><td> #DBDBDB</td></tr>
    <tr bgcolor="#DEDEDE"><td>grey87 </td><td>222 </td><td>222 </td><td>222</td><td> #DEDEDE</td></tr>
    <tr bgcolor="#E0E0E0"><td>grey88 </td><td>224 </td><td>224 </td><td>224</td><td> #E0E0E0</td></tr>
    <tr bgcolor="#E3E3E3"><td>grey89 </td><td>227 </td><td>227 </td><td>227</td><td> #E3E3E3</td></tr>
    <tr bgcolor="#E5E5E5"><td>grey90 </td><td>229 </td><td>229 </td><td>229</td><td> #E5E5E5</td></tr>
    <tr bgcolor="#E8E8E8"><td>grey91 </td><td>232 </td><td>232 </td><td>232</td><td> #E8E8E8</td></tr>
    <tr bgcolor="#EBEBEB"><td>grey92 </td><td>235 </td><td>235 </td><td>235</td><td> #EBEBEB</td></tr>
    <tr bgcolor="#EDEDED"><td>grey93 </td><td>237 </td><td>237 </td><td>237</td><td> #EDEDED</td></tr>
    <tr bgcolor="#F0F0F0"><td>grey94 </td><td>240 </td><td>240 </td><td>240</td><td> #F0F0F0</td></tr>
    <tr bgcolor="#F2F2F2"><td>grey95 </td><td>242 </td><td>242 </td><td>242</td><td> #F2F2F2</td></tr>
    <tr bgcolor="#F5F5F5"><td>grey96 </td><td>245 </td><td>245 </td><td>245</td><td> #F5F5F5</td></tr>
    <tr bgcolor="#F7F7F7"><td>grey97 </td><td>247 </td><td>247 </td><td>247</td><td> #F7F7F7</td></tr>
    <tr bgcolor="#FAFAFA"><td>grey98 </td><td>250 </td><td>250 </td><td>250</td><td> #FAFAFA</td></tr>
    <tr bgcolor="#FCFCFC"><td>grey99 </td><td>252 </td><td>252 </td><td>252</td><td> #FCFCFC</td></tr>
    <tr bgcolor="#FFFFFF"><td>grey100 </td><td>255 </td><td>255 </td><td>255</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#F0F0FF"><td>honeydew </td><td>240 </td><td>255 </td><td>240</td><td> #F0F0FF</td></tr>
    <tr bgcolor="#F0F0FF"><td>honeydew1 </td><td>240 </td><td>255 </td><td>240</td><td> #F0F0FF</td></tr>
    <tr bgcolor="#E0E0EE"><td>honeydew2 </td><td>224 </td><td>238 </td><td>224</td><td> #E0E0EE</td></tr>
    <tr bgcolor="#C1C1CD"><td>honeydew3 </td><td>193 </td><td>205 </td><td>193</td><td> #C1C1CD</td></tr>
    <tr bgcolor="#83838B"><td>honeydew4 </td><td>131 </td><td>139 </td><td>131</td><td> #83838B</td></tr>
    <tr bgcolor="#FFFF69"><td>hot pink </td><td>255 </td><td>105 </td><td>180</td><td> #FFFF69</td></tr>
    <tr bgcolor="#FFFF69"><td>HotPink </td><td>255 </td><td>105 </td><td>180</td><td> #FFFF69</td></tr>
    <tr bgcolor="#FFFF6E"><td>HotPink1 </td><td>255 </td><td>110 </td><td>180</td><td> #FFFF6E</td></tr>
    <tr bgcolor="#EEEE6A"><td>HotPink2 </td><td>238 </td><td>106 </td><td>167</td><td> #EEEE6A</td></tr>
    <tr bgcolor="#CDCD60"><td>HotPink3 </td><td>205 </td><td>96 </td><td>144</td><td> #CDCD60</td></tr>
    <tr bgcolor="#8B8B3A"><td>HotPink4 </td><td>139 </td><td>58 </td><td>98</td><td> #8B8B3A</td></tr>
    <tr bgcolor="#CDCD5C"><td>indian red </td><td>205 </td><td>92 </td><td>92</td><td> #CDCD5C</td></tr>
    <tr bgcolor="#CDCD5C"><td>IndianRed </td><td>205 </td><td>92 </td><td>92</td><td> #CDCD5C</td></tr>
    <tr bgcolor="#FFFF6A"><td>IndianRed1 </td><td>255 </td><td>106 </td><td>106</td><td> #FFFF6A</td></tr>
    <tr bgcolor="#EEEE63"><td>IndianRed2 </td><td>238 </td><td>99 </td><td>99</td><td> #EEEE63</td></tr>
    <tr bgcolor="#CDCD55"><td>IndianRed3 </td><td>205 </td><td>85 </td><td>85</td><td> #CDCD55</td></tr>
    <tr bgcolor="#8B8B3A"><td>IndianRed4 </td><td>139 </td><td>58 </td><td>58</td><td> #8B8B3A</td></tr>
    <tr bgcolor="#4B4B00"><td>indigo </td><td>75 </td><td>0 </td><td>130</td><td> #4B4B00</td></tr>
    <tr bgcolor="#FFFFFF"><td>ivory </td><td>255 </td><td>255 </td><td>240</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#FFFFFF"><td>ivory1 </td><td>255 </td><td>255 </td><td>240</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#EEEEEE"><td>ivory2 </td><td>238 </td><td>238 </td><td>224</td><td> #EEEEEE</td></tr>
    <tr bgcolor="#CDCDCD"><td>ivory3 </td><td>205 </td><td>205 </td><td>193</td><td> #CDCDCD</td></tr>
    <tr bgcolor="#8B8B8B"><td>ivory4 </td><td>139 </td><td>139 </td><td>131</td><td> #8B8B8B</td></tr>
    <tr bgcolor="#F0F0E6"><td>khaki </td><td>240 </td><td>230 </td><td>140</td><td> #F0F0E6</td></tr>
    <tr bgcolor="#FFFFF6"><td>khaki1 </td><td>255 </td><td>246 </td><td>143</td><td> #FFFFF6</td></tr>
    <tr bgcolor="#EEEEE6"><td>khaki2 </td><td>238 </td><td>230 </td><td>133</td><td> #EEEEE6</td></tr>
    <tr bgcolor="#CDCDC6"><td>khaki3 </td><td>205 </td><td>198 </td><td>115</td><td> #CDCDC6</td></tr>
    <tr bgcolor="#8B8B86"><td>khaki4 </td><td>139 </td><td>134 </td><td>78</td><td> #8B8B86</td></tr>
    <tr bgcolor="#E6E6E6"><td>lavender </td><td>230 </td><td>230 </td><td>250</td><td> #E6E6E6</td></tr>
    <tr bgcolor="#FFFFF0"><td>lavender blush </td><td>255 </td><td>240 </td><td>245</td><td> #FFFFF0</td></tr>
    <tr bgcolor="#FFFFF0"><td>LavenderBlush </td><td>255 </td><td>240 </td><td>245</td><td> #FFFFF0</td></tr>
    <tr bgcolor="#FFFFF0"><td>LavenderBlush1 </td><td>255 </td><td>240 </td><td>245</td><td> #FFFFF0</td></tr>
    <tr bgcolor="#EEEEE0"><td>LavenderBlush2 </td><td>238 </td><td>224 </td><td>229</td><td> #EEEEE0</td></tr>
    <tr bgcolor="#CDCDC1"><td>LavenderBlush3 </td><td>205 </td><td>193 </td><td>197</td><td> #CDCDC1</td></tr>
    <tr bgcolor="#8B8B83"><td>LavenderBlush4 </td><td>139 </td><td>131 </td><td>134</td><td> #8B8B83</td></tr>
    <tr bgcolor="#7C7CFC"><td>lawn green </td><td>124 </td><td>252 </td><td>0</td><td> #7C7CFC</td></tr>
    <tr bgcolor="#7C7CFC"><td>LawnGreen </td><td>124 </td><td>252 </td><td>0</td><td> #7C7CFC</td></tr>
    <tr bgcolor="#FFFFFA"><td>lemon chiffon </td><td>255 </td><td>250 </td><td>205</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#FFFFFA"><td>LemonChiffon </td><td>255 </td><td>250 </td><td>205</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#FFFFFA"><td>LemonChiffon1 </td><td>255 </td><td>250 </td><td>205</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#EEEEE9"><td>LemonChiffon2 </td><td>238 </td><td>233 </td><td>191</td><td> #EEEEE9</td></tr>
    <tr bgcolor="#CDCDC9"><td>LemonChiffon3 </td><td>205 </td><td>201 </td><td>165</td><td> #CDCDC9</td></tr>
    <tr bgcolor="#8B8B89"><td>LemonChiffon4 </td><td>139 </td><td>137 </td><td>112</td><td> #8B8B89</td></tr>
    <tr bgcolor="#ADADD8"><td>light blue </td><td>173 </td><td>216 </td><td>230</td><td> #ADADD8</td></tr>
    <tr bgcolor="#F0F080"><td>light coral </td><td>240 </td><td>128 </td><td>128</td><td> #F0F080</td></tr>
    <tr bgcolor="#E0E0FF"><td>light cyan </td><td>224 </td><td>255 </td><td>255</td><td> #E0E0FF</td></tr>
    <tr bgcolor="#EEEEDD"><td>light goldenrod </td><td>238 </td><td>221 </td><td>130</td><td> #EEEEDD</td></tr>
    <tr bgcolor="#FAFAFA"><td>light goldenrod yellow </td><td>250 </td><td>250 </td><td>210</td><td> #FAFAFA</td></tr>
    <tr bgcolor="#D3D3D3"><td>light gray </td><td>211 </td><td>211 </td><td>211</td><td> #D3D3D3</td></tr>
    <tr bgcolor="#9090EE"><td>light green </td><td>144 </td><td>238 </td><td>144</td><td> #9090EE</td></tr>
    <tr bgcolor="#D3D3D3"><td>light grey </td><td>211 </td><td>211 </td><td>211</td><td> #D3D3D3</td></tr>
    <tr bgcolor="#FFFFB6"><td>light pink </td><td>255 </td><td>182 </td><td>193</td><td> #FFFFB6</td></tr>
    <tr bgcolor="#FFFFA0"><td>light salmon </td><td>255 </td><td>160 </td><td>122</td><td> #FFFFA0</td></tr>
    <tr bgcolor="#2020B2"><td>light sea green </td><td>32 </td><td>178 </td><td>170</td><td> #2020B2</td></tr>
    <tr bgcolor="#8787CE"><td>light sky blue </td><td>135 </td><td>206 </td><td>250</td><td> #8787CE</td></tr>
    <tr bgcolor="#848470"><td>light slate blue </td><td>132 </td><td>112 </td><td>255</td><td> #848470</td></tr>
    <tr bgcolor="#777788"><td>light slate gray </td><td>119 </td><td>136 </td><td>153</td><td> #777788</td></tr>
    <tr bgcolor="#777788"><td>light slate grey </td><td>119 </td><td>136 </td><td>153</td><td> #777788</td></tr>
    <tr bgcolor="#B0B0C4"><td>light steel blue </td><td>176 </td><td>196 </td><td>222</td><td> #B0B0C4</td></tr>
    <tr bgcolor="#FFFFFF"><td>light yellow </td><td>255 </td><td>255 </td><td>224</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#ADADD8"><td>LightBlue </td><td>173 </td><td>216 </td><td>230</td><td> #ADADD8</td></tr>
    <tr bgcolor="#BFBFEF"><td>LightBlue1 </td><td>191 </td><td>239 </td><td>255</td><td> #BFBFEF</td></tr>
    <tr bgcolor="#B2B2DF"><td>LightBlue2 </td><td>178 </td><td>223 </td><td>238</td><td> #B2B2DF</td></tr>
    <tr bgcolor="#9A9AC0"><td>LightBlue3 </td><td>154 </td><td>192 </td><td>205</td><td> #9A9AC0</td></tr>
    <tr bgcolor="#686883"><td>LightBlue4 </td><td>104 </td><td>131 </td><td>139</td><td> #686883</td></tr>
    <tr bgcolor="#F0F080"><td>LightCoral </td><td>240 </td><td>128 </td><td>128</td><td> #F0F080</td></tr>
    <tr bgcolor="#E0E0FF"><td>LightCyan </td><td>224 </td><td>255 </td><td>255</td><td> #E0E0FF</td></tr>
    <tr bgcolor="#E0E0FF"><td>LightCyan1 </td><td>224 </td><td>255 </td><td>255</td><td> #E0E0FF</td></tr>
    <tr bgcolor="#D1D1EE"><td>LightCyan2 </td><td>209 </td><td>238 </td><td>238</td><td> #D1D1EE</td></tr>
    <tr bgcolor="#B4B4CD"><td>LightCyan3 </td><td>180 </td><td>205 </td><td>205</td><td> #B4B4CD</td></tr>
    <tr bgcolor="#7A7A8B"><td>LightCyan4 </td><td>122 </td><td>139 </td><td>139</td><td> #7A7A8B</td></tr>
    <tr bgcolor="#EEEEDD"><td>LightGoldenrod </td><td>238 </td><td>221 </td><td>130</td><td> #EEEEDD</td></tr>
    <tr bgcolor="#FFFFEC"><td>LightGoldenrod1 </td><td>255 </td><td>236 </td><td>139</td><td> #FFFFEC</td></tr>
    <tr bgcolor="#EEEEDC"><td>LightGoldenrod2 </td><td>238 </td><td>220 </td><td>130</td><td> #EEEEDC</td></tr>
    <tr bgcolor="#CDCDBE"><td>LightGoldenrod3 </td><td>205 </td><td>190 </td><td>112</td><td> #CDCDBE</td></tr>
    <tr bgcolor="#8B8B81"><td>LightGoldenrod4 </td><td>139 </td><td>129 </td><td>76</td><td> #8B8B81</td></tr>
    <tr bgcolor="#FAFAFA"><td>LightGoldenrodYellow </td><td>250 </td><td>250 </td><td>210</td><td> #FAFAFA</td></tr>
    <tr bgcolor="#D3D3D3"><td>LightGray </td><td>211 </td><td>211 </td><td>211</td><td> #D3D3D3</td></tr>
    <tr bgcolor="#9090EE"><td>LightGreen </td><td>144 </td><td>238 </td><td>144</td><td> #9090EE</td></tr>
    <tr bgcolor="#D3D3D3"><td>LightGrey </td><td>211 </td><td>211 </td><td>211</td><td> #D3D3D3</td></tr>
    <tr bgcolor="#FFFFB6"><td>LightPink </td><td>255 </td><td>182 </td><td>193</td><td> #FFFFB6</td></tr>
    <tr bgcolor="#FFFFAE"><td>LightPink1 </td><td>255 </td><td>174 </td><td>185</td><td> #FFFFAE</td></tr>
    <tr bgcolor="#EEEEA2"><td>LightPink2 </td><td>238 </td><td>162 </td><td>173</td><td> #EEEEA2</td></tr>
    <tr bgcolor="#CDCD8C"><td>LightPink3 </td><td>205 </td><td>140 </td><td>149</td><td> #CDCD8C</td></tr>
    <tr bgcolor="#8B8B5F"><td>LightPink4 </td><td>139 </td><td>95 </td><td>101</td><td> #8B8B5F</td></tr>
    <tr bgcolor="#FFFFA0"><td>LightSalmon </td><td>255 </td><td>160 </td><td>122</td><td> #FFFFA0</td></tr>
    <tr bgcolor="#FFFFA0"><td>LightSalmon1 </td><td>255 </td><td>160 </td><td>122</td><td> #FFFFA0</td></tr>
    <tr bgcolor="#EEEE95"><td>LightSalmon2 </td><td>238 </td><td>149 </td><td>114</td><td> #EEEE95</td></tr>
    <tr bgcolor="#CDCD81"><td>LightSalmon3 </td><td>205 </td><td>129 </td><td>98</td><td> #CDCD81</td></tr>
    <tr bgcolor="#8B8B57"><td>LightSalmon4 </td><td>139 </td><td>87 </td><td>66</td><td> #8B8B57</td></tr>
    <tr bgcolor="#2020B2"><td>LightSeaGreen </td><td>32 </td><td>178 </td><td>170</td><td> #2020B2</td></tr>
    <tr bgcolor="#8787CE"><td>LightSkyBlue </td><td>135 </td><td>206 </td><td>250</td><td> #8787CE</td></tr>
    <tr bgcolor="#B0B0E2"><td>LightSkyBlue1 </td><td>176 </td><td>226 </td><td>255</td><td> #B0B0E2</td></tr>
    <tr bgcolor="#A4A4D3"><td>LightSkyBlue2 </td><td>164 </td><td>211 </td><td>238</td><td> #A4A4D3</td></tr>
    <tr bgcolor="#8D8DB6"><td>LightSkyBlue3 </td><td>141 </td><td>182 </td><td>205</td><td> #8D8DB6</td></tr>
    <tr bgcolor="#60607B"><td>LightSkyBlue4 </td><td>96 </td><td>123 </td><td>139</td><td> #60607B</td></tr>
    <tr bgcolor="#848470"><td>LightSlateBlue </td><td>132 </td><td>112 </td><td>255</td><td> #848470</td></tr>
    <tr bgcolor="#777788"><td>LightSlateGray </td><td>119 </td><td>136 </td><td>153</td><td> #777788</td></tr>
    <tr bgcolor="#777788"><td>LightSlateGrey </td><td>119 </td><td>136 </td><td>153</td><td> #777788</td></tr>
    <tr bgcolor="#B0B0C4"><td>LightSteelBlue </td><td>176 </td><td>196 </td><td>222</td><td> #B0B0C4</td></tr>
    <tr bgcolor="#CACAE1"><td>LightSteelBlue1 </td><td>202 </td><td>225 </td><td>255</td><td> #CACAE1</td></tr>
    <tr bgcolor="#BCBCD2"><td>LightSteelBlue2 </td><td>188 </td><td>210 </td><td>238</td><td> #BCBCD2</td></tr>
    <tr bgcolor="#A2A2B5"><td>LightSteelBlue3 </td><td>162 </td><td>181 </td><td>205</td><td> #A2A2B5</td></tr>
    <tr bgcolor="#6E6E7B"><td>LightSteelBlue4 </td><td>110 </td><td>123 </td><td>139</td><td> #6E6E7B</td></tr>
    <tr bgcolor="#FFFFFF"><td>LightYellow </td><td>255 </td><td>255 </td><td>224</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#FFFFFF"><td>LightYellow1 </td><td>255 </td><td>255 </td><td>224</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#EEEEEE"><td>LightYellow2 </td><td>238 </td><td>238 </td><td>209</td><td> #EEEEEE</td></tr>
    <tr bgcolor="#CDCDCD"><td>LightYellow3 </td><td>205 </td><td>205 </td><td>180</td><td> #CDCDCD</td></tr>
    <tr bgcolor="#8B8B8B"><td>LightYellow4 </td><td>139 </td><td>139 </td><td>122</td><td> #8B8B8B</td></tr>
    <tr bgcolor="#0000FF"><td>lime </td><td>0 </td><td>255 </td><td>0</td><td> #0000FF</td></tr>
    <tr bgcolor="#3232CD"><td>lime green </td><td>50 </td><td>205 </td><td>50</td><td> #3232CD</td></tr>
    <tr bgcolor="#3232CD"><td>LimeGreen </td><td>50 </td><td>205 </td><td>50</td><td> #3232CD</td></tr>
    <tr bgcolor="#FAFAF0"><td>linen </td><td>250 </td><td>240 </td><td>230</td><td> #FAFAF0</td></tr>
    <tr bgcolor="#FFFF00"><td>magenta </td><td>255 </td><td>0 </td><td>255</td><td> #FFFF00</td></tr>
    <tr bgcolor="#FFFF00"><td>magenta1 </td><td>255 </td><td>0 </td><td>255</td><td> #FFFF00</td></tr>
    <tr bgcolor="#EEEE00"><td>magenta2 </td><td>238 </td><td>0 </td><td>238</td><td> #EEEE00</td></tr>
    <tr bgcolor="#CDCD00"><td>magenta3 </td><td>205 </td><td>0 </td><td>205</td><td> #CDCD00</td></tr>
    <tr bgcolor="#8B8B00"><td>magenta4 </td><td>139 </td><td>0 </td><td>139</td><td> #8B8B00</td></tr>
    <tr bgcolor="#808000"><td>maroon </td><td>128 </td><td>0 </td><td>0</td><td> #808000</td></tr>
    <tr bgcolor="#FFFF34"><td>maroon1 </td><td>255 </td><td>52 </td><td>179</td><td> #FFFF34</td></tr>
    <tr bgcolor="#EEEE30"><td>maroon2 </td><td>238 </td><td>48 </td><td>167</td><td> #EEEE30</td></tr>
    <tr bgcolor="#CDCD29"><td>maroon3 </td><td>205 </td><td>41 </td><td>144</td><td> #CDCD29</td></tr>
    <tr bgcolor="#8B8B1C"><td>maroon4 </td><td>139 </td><td>28 </td><td>98</td><td> #8B8B1C</td></tr>
    <tr bgcolor="#6666CD"><td>medium aquamarine </td><td>102 </td><td>205 </td><td>170</td><td> #6666CD</td></tr>
    <tr bgcolor="#000000"><td>medium blue </td><td>0 </td><td>0 </td><td>205</td><td> #000000</td></tr>
    <tr bgcolor="#BABA55"><td>medium orchid </td><td>186 </td><td>85 </td><td>211</td><td> #BABA55</td></tr>
    <tr bgcolor="#939370"><td>medium purple </td><td>147 </td><td>112 </td><td>219</td><td> #939370</td></tr>
    <tr bgcolor="#3C3CB3"><td>medium sea green </td><td>60 </td><td>179 </td><td>113</td><td> #3C3CB3</td></tr>
    <tr bgcolor="#7B7B68"><td>medium slate blue </td><td>123 </td><td>104 </td><td>238</td><td> #7B7B68</td></tr>
    <tr bgcolor="#0000FA"><td>medium spring green </td><td>0 </td><td>250 </td><td>154</td><td> #0000FA</td></tr>
    <tr bgcolor="#4848D1"><td>medium turquoise </td><td>72 </td><td>209 </td><td>204</td><td> #4848D1</td></tr>
    <tr bgcolor="#C7C715"><td>medium violet red </td><td>199 </td><td>21 </td><td>133</td><td> #C7C715</td></tr>
    <tr bgcolor="#6666CD"><td>MediumAquamarine </td><td>102 </td><td>205 </td><td>170</td><td> #6666CD</td></tr>
    <tr bgcolor="#000000"><td>MediumBlue </td><td>0 </td><td>0 </td><td>205</td><td> #000000</td></tr>
    <tr bgcolor="#BABA55"><td>MediumOrchid </td><td>186 </td><td>85 </td><td>211</td><td> #BABA55</td></tr>
    <tr bgcolor="#E0E066"><td>MediumOrchid1 </td><td>224 </td><td>102 </td><td>255</td><td> #E0E066</td></tr>
    <tr bgcolor="#D1D15F"><td>MediumOrchid2 </td><td>209 </td><td>95 </td><td>238</td><td> #D1D15F</td></tr>
    <tr bgcolor="#B4B452"><td>MediumOrchid3 </td><td>180 </td><td>82 </td><td>205</td><td> #B4B452</td></tr>
    <tr bgcolor="#7A7A37"><td>MediumOrchid4 </td><td>122 </td><td>55 </td><td>139</td><td> #7A7A37</td></tr>
    <tr bgcolor="#939370"><td>MediumPurple </td><td>147 </td><td>112 </td><td>219</td><td> #939370</td></tr>
    <tr bgcolor="#ABAB82"><td>MediumPurple1 </td><td>171 </td><td>130 </td><td>255</td><td> #ABAB82</td></tr>
    <tr bgcolor="#9F9F79"><td>MediumPurple2 </td><td>159 </td><td>121 </td><td>238</td><td> #9F9F79</td></tr>
    <tr bgcolor="#898968"><td>MediumPurple3 </td><td>137 </td><td>104 </td><td>205</td><td> #898968</td></tr>
    <tr bgcolor="#5D5D47"><td>MediumPurple4 </td><td>93 </td><td>71 </td><td>139</td><td> #5D5D47</td></tr>
    <tr bgcolor="#3C3CB3"><td>MediumSeaGreen </td><td>60 </td><td>179 </td><td>113</td><td> #3C3CB3</td></tr>
    <tr bgcolor="#7B7B68"><td>MediumSlateBlue </td><td>123 </td><td>104 </td><td>238</td><td> #7B7B68</td></tr>
    <tr bgcolor="#0000FA"><td>MediumSpringGreen </td><td>0 </td><td>250 </td><td>154</td><td> #0000FA</td></tr>
    <tr bgcolor="#4848D1"><td>MediumTurquoise </td><td>72 </td><td>209 </td><td>204</td><td> #4848D1</td></tr>
    <tr bgcolor="#C7C715"><td>MediumVioletRed </td><td>199 </td><td>21 </td><td>133</td><td> #C7C715</td></tr>
    <tr bgcolor="#191919"><td>midnight blue </td><td>25 </td><td>25 </td><td>112</td><td> #191919</td></tr>
    <tr bgcolor="#191919"><td>MidnightBlue </td><td>25 </td><td>25 </td><td>112</td><td> #191919</td></tr>
    <tr bgcolor="#F5F5FF"><td>mint cream </td><td>245 </td><td>255 </td><td>250</td><td> #F5F5FF</td></tr>
    <tr bgcolor="#F5F5FF"><td>MintCream </td><td>245 </td><td>255 </td><td>250</td><td> #F5F5FF</td></tr>
    <tr bgcolor="#FFFFE4"><td>misty rose </td><td>255 </td><td>228 </td><td>225</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#FFFFE4"><td>MistyRose </td><td>255 </td><td>228 </td><td>225</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#FFFFE4"><td>MistyRose1 </td><td>255 </td><td>228 </td><td>225</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#EEEED5"><td>MistyRose2 </td><td>238 </td><td>213 </td><td>210</td><td> #EEEED5</td></tr>
    <tr bgcolor="#CDCDB7"><td>MistyRose3 </td><td>205 </td><td>183 </td><td>181</td><td> #CDCDB7</td></tr>
    <tr bgcolor="#8B8B7D"><td>MistyRose4 </td><td>139 </td><td>125 </td><td>123</td><td> #8B8B7D</td></tr>
    <tr bgcolor="#FFFFE4"><td>moccasin </td><td>255 </td><td>228 </td><td>181</td><td> #FFFFE4</td></tr>
    <tr bgcolor="#FFFFDE"><td>navajo white </td><td>255 </td><td>222 </td><td>173</td><td> #FFFFDE</td></tr>
    <tr bgcolor="#FFFFDE"><td>NavajoWhite </td><td>255 </td><td>222 </td><td>173</td><td> #FFFFDE</td></tr>
    <tr bgcolor="#FFFFDE"><td>NavajoWhite1 </td><td>255 </td><td>222 </td><td>173</td><td> #FFFFDE</td></tr>
    <tr bgcolor="#EEEECF"><td>NavajoWhite2 </td><td>238 </td><td>207 </td><td>161</td><td> #EEEECF</td></tr>
    <tr bgcolor="#CDCDB3"><td>NavajoWhite3 </td><td>205 </td><td>179 </td><td>139</td><td> #CDCDB3</td></tr>
    <tr bgcolor="#8B8B79"><td>NavajoWhite4 </td><td>139 </td><td>121 </td><td>94</td><td> #8B8B79</td></tr>
    <tr bgcolor="#000000"><td>navy </td><td>0 </td><td>0 </td><td>128</td><td> #000000</td></tr>
    <tr bgcolor="#000000"><td>navy blue </td><td>0 </td><td>0 </td><td>128</td><td> #000000</td></tr>
    <tr bgcolor="#000000"><td>NavyBlue </td><td>0 </td><td>0 </td><td>128</td><td> #000000</td></tr>
    <tr bgcolor="#FDFDF5"><td>old lace </td><td>253 </td><td>245 </td><td>230</td><td> #FDFDF5</td></tr>
    <tr bgcolor="#FDFDF5"><td>OldLace </td><td>253 </td><td>245 </td><td>230</td><td> #FDFDF5</td></tr>
    <tr bgcolor="#808080"><td>olive </td><td>128 </td><td>128 </td><td>0</td><td> #808080</td></tr>
    <tr bgcolor="#6B6B8E"><td>olive drab </td><td>107 </td><td>142 </td><td>35</td><td> #6B6B8E</td></tr>
    <tr bgcolor="#6B6B8E"><td>OliveDrab </td><td>107 </td><td>142 </td><td>35</td><td> #6B6B8E</td></tr>
    <tr bgcolor="#C0C0FF"><td>OliveDrab1 </td><td>192 </td><td>255 </td><td>62</td><td> #C0C0FF</td></tr>
    <tr bgcolor="#B3B3EE"><td>OliveDrab2 </td><td>179 </td><td>238 </td><td>58</td><td> #B3B3EE</td></tr>
    <tr bgcolor="#9A9ACD"><td>OliveDrab3 </td><td>154 </td><td>205 </td><td>50</td><td> #9A9ACD</td></tr>
    <tr bgcolor="#69698B"><td>OliveDrab4 </td><td>105 </td><td>139 </td><td>34</td><td> #69698B</td></tr>
    <tr bgcolor="#FFFFA5"><td>orange </td><td>255 </td><td>165 </td><td>0</td><td> #FFFFA5</td></tr>
    <tr bgcolor="#FFFF45"><td>orange red </td><td>255 </td><td>69 </td><td>0</td><td> #FFFF45</td></tr>
    <tr bgcolor="#FFFFA5"><td>orange1 </td><td>255 </td><td>165 </td><td>0</td><td> #FFFFA5</td></tr>
    <tr bgcolor="#EEEE9A"><td>orange2 </td><td>238 </td><td>154 </td><td>0</td><td> #EEEE9A</td></tr>
    <tr bgcolor="#CDCD85"><td>orange3 </td><td>205 </td><td>133 </td><td>0</td><td> #CDCD85</td></tr>
    <tr bgcolor="#8B8B5A"><td>orange4 </td><td>139 </td><td>90 </td><td>0</td><td> #8B8B5A</td></tr>
    <tr bgcolor="#FFFF45"><td>OrangeRed </td><td>255 </td><td>69 </td><td>0</td><td> #FFFF45</td></tr>
    <tr bgcolor="#FFFF45"><td>OrangeRed1 </td><td>255 </td><td>69 </td><td>0</td><td> #FFFF45</td></tr>
    <tr bgcolor="#EEEE40"><td>OrangeRed2 </td><td>238 </td><td>64 </td><td>0</td><td> #EEEE40</td></tr>
    <tr bgcolor="#CDCD37"><td>OrangeRed3 </td><td>205 </td><td>55 </td><td>0</td><td> #CDCD37</td></tr>
    <tr bgcolor="#8B8B25"><td>OrangeRed4 </td><td>139 </td><td>37 </td><td>0</td><td> #8B8B25</td></tr>
    <tr bgcolor="#DADA70"><td>orchid </td><td>218 </td><td>112 </td><td>214</td><td> #DADA70</td></tr>
    <tr bgcolor="#FFFF83"><td>orchid1 </td><td>255 </td><td>131 </td><td>250</td><td> #FFFF83</td></tr>
    <tr bgcolor="#EEEE7A"><td>orchid2 </td><td>238 </td><td>122 </td><td>233</td><td> #EEEE7A</td></tr>
    <tr bgcolor="#CDCD69"><td>orchid3 </td><td>205 </td><td>105 </td><td>201</td><td> #CDCD69</td></tr>
    <tr bgcolor="#8B8B47"><td>orchid4 </td><td>139 </td><td>71 </td><td>137</td><td> #8B8B47</td></tr>
    <tr bgcolor="#EEEEE8"><td>pale goldenrod </td><td>238 </td><td>232 </td><td>170</td><td> #EEEEE8</td></tr>
    <tr bgcolor="#9898FB"><td>pale green </td><td>152 </td><td>251 </td><td>152</td><td> #9898FB</td></tr>
    <tr bgcolor="#AFAFEE"><td>pale turquoise </td><td>175 </td><td>238 </td><td>238</td><td> #AFAFEE</td></tr>
    <tr bgcolor="#DBDB70"><td>pale violet red </td><td>219 </td><td>112 </td><td>147</td><td> #DBDB70</td></tr>
    <tr bgcolor="#EEEEE8"><td>PaleGoldenrod </td><td>238 </td><td>232 </td><td>170</td><td> #EEEEE8</td></tr>
    <tr bgcolor="#9898FB"><td>PaleGreen </td><td>152 </td><td>251 </td><td>152</td><td> #9898FB</td></tr>
    <tr bgcolor="#9A9AFF"><td>PaleGreen1 </td><td>154 </td><td>255 </td><td>154</td><td> #9A9AFF</td></tr>
    <tr bgcolor="#9090EE"><td>PaleGreen2 </td><td>144 </td><td>238 </td><td>144</td><td> #9090EE</td></tr>
    <tr bgcolor="#7C7CCD"><td>PaleGreen3 </td><td>124 </td><td>205 </td><td>124</td><td> #7C7CCD</td></tr>
    <tr bgcolor="#54548B"><td>PaleGreen4 </td><td>84 </td><td>139 </td><td>84</td><td> #54548B</td></tr>
    <tr bgcolor="#AFAFEE"><td>PaleTurquoise </td><td>175 </td><td>238 </td><td>238</td><td> #AFAFEE</td></tr>
    <tr bgcolor="#BBBBFF"><td>PaleTurquoise1 </td><td>187 </td><td>255 </td><td>255</td><td> #BBBBFF</td></tr>
    <tr bgcolor="#AEAEEE"><td>PaleTurquoise2 </td><td>174 </td><td>238 </td><td>238</td><td> #AEAEEE</td></tr>
    <tr bgcolor="#9696CD"><td>PaleTurquoise3 </td><td>150 </td><td>205 </td><td>205</td><td> #9696CD</td></tr>
    <tr bgcolor="#66668B"><td>PaleTurquoise4 </td><td>102 </td><td>139 </td><td>139</td><td> #66668B</td></tr>
    <tr bgcolor="#DBDB70"><td>PaleVioletRed </td><td>219 </td><td>112 </td><td>147</td><td> #DBDB70</td></tr>
    <tr bgcolor="#FFFF82"><td>PaleVioletRed1 </td><td>255 </td><td>130 </td><td>171</td><td> #FFFF82</td></tr>
    <tr bgcolor="#EEEE79"><td>PaleVioletRed2 </td><td>238 </td><td>121 </td><td>159</td><td> #EEEE79</td></tr>
    <tr bgcolor="#CDCD68"><td>PaleVioletRed3 </td><td>205 </td><td>104 </td><td>127</td><td> #CDCD68</td></tr>
    <tr bgcolor="#8B8B47"><td>PaleVioletRed4 </td><td>139 </td><td>71 </td><td>93</td><td> #8B8B47</td></tr>
    <tr bgcolor="#FFFFEF"><td>papaya whip </td><td>255 </td><td>239 </td><td>213</td><td> #FFFFEF</td></tr>
    <tr bgcolor="#FFFFEF"><td>PapayaWhip </td><td>255 </td><td>239 </td><td>213</td><td> #FFFFEF</td></tr>
    <tr bgcolor="#FFFFDA"><td>peach puff </td><td>255 </td><td>218 </td><td>185</td><td> #FFFFDA</td></tr>
    <tr bgcolor="#FFFFDA"><td>PeachPuff </td><td>255 </td><td>218 </td><td>185</td><td> #FFFFDA</td></tr>
    <tr bgcolor="#FFFFDA"><td>PeachPuff1 </td><td>255 </td><td>218 </td><td>185</td><td> #FFFFDA</td></tr>
    <tr bgcolor="#EEEECB"><td>PeachPuff2 </td><td>238 </td><td>203 </td><td>173</td><td> #EEEECB</td></tr>
    <tr bgcolor="#CDCDAF"><td>PeachPuff3 </td><td>205 </td><td>175 </td><td>149</td><td> #CDCDAF</td></tr>
    <tr bgcolor="#8B8B77"><td>PeachPuff4 </td><td>139 </td><td>119 </td><td>101</td><td> #8B8B77</td></tr>
    <tr bgcolor="#CDCD85"><td>peru </td><td>205 </td><td>133 </td><td>63</td><td> #CDCD85</td></tr>
    <tr bgcolor="#FFFFC0"><td>pink </td><td>255 </td><td>192 </td><td>203</td><td> #FFFFC0</td></tr>
    <tr bgcolor="#FFFFB5"><td>pink1 </td><td>255 </td><td>181 </td><td>197</td><td> #FFFFB5</td></tr>
    <tr bgcolor="#EEEEA9"><td>pink2 </td><td>238 </td><td>169 </td><td>184</td><td> #EEEEA9</td></tr>
    <tr bgcolor="#CDCD91"><td>pink3 </td><td>205 </td><td>145 </td><td>158</td><td> #CDCD91</td></tr>
    <tr bgcolor="#8B8B63"><td>pink4 </td><td>139 </td><td>99 </td><td>108</td><td> #8B8B63</td></tr>
    <tr bgcolor="#DDDDA0"><td>plum </td><td>221 </td><td>160 </td><td>221</td><td> #DDDDA0</td></tr>
    <tr bgcolor="#FFFFBB"><td>plum1 </td><td>255 </td><td>187 </td><td>255</td><td> #FFFFBB</td></tr>
    <tr bgcolor="#EEEEAE"><td>plum2 </td><td>238 </td><td>174 </td><td>238</td><td> #EEEEAE</td></tr>
    <tr bgcolor="#CDCD96"><td>plum3 </td><td>205 </td><td>150 </td><td>205</td><td> #CDCD96</td></tr>
    <tr bgcolor="#8B8B66"><td>plum4 </td><td>139 </td><td>102 </td><td>139</td><td> #8B8B66</td></tr>
    <tr bgcolor="#B0B0E0"><td>powder blue </td><td>176 </td><td>224 </td><td>230</td><td> #B0B0E0</td></tr>
    <tr bgcolor="#B0B0E0"><td>PowderBlue </td><td>176 </td><td>224 </td><td>230</td><td> #B0B0E0</td></tr>
    <tr bgcolor="#808000"><td>purple </td><td>128 </td><td>0 </td><td>128</td><td> #808000</td></tr>
    <tr bgcolor="#9B9B30"><td>purple1 </td><td>155 </td><td>48 </td><td>255</td><td> #9B9B30</td></tr>
    <tr bgcolor="#91912C"><td>purple2 </td><td>145 </td><td>44 </td><td>238</td><td> #91912C</td></tr>
    <tr bgcolor="#7D7D26"><td>purple3 </td><td>125 </td><td>38 </td><td>205</td><td> #7D7D26</td></tr>
    <tr bgcolor="#55551A"><td>purple4 </td><td>85 </td><td>26 </td><td>139</td><td> #55551A</td></tr>
    <tr bgcolor="#FFFF00"><td>red </td><td>255 </td><td>0 </td><td>0</td><td> #FFFF00</td></tr>
    <tr bgcolor="#FFFF00"><td>red1 </td><td>255 </td><td>0 </td><td>0</td><td> #FFFF00</td></tr>
    <tr bgcolor="#EEEE00"><td>red2 </td><td>238 </td><td>0 </td><td>0</td><td> #EEEE00</td></tr>
    <tr bgcolor="#CDCD00"><td>red3 </td><td>205 </td><td>0 </td><td>0</td><td> #CDCD00</td></tr>
    <tr bgcolor="#8B8B00"><td>red4 </td><td>139 </td><td>0 </td><td>0</td><td> #8B8B00</td></tr>
    <tr bgcolor="#BCBC8F"><td>rosy brown </td><td>188 </td><td>143 </td><td>143</td><td> #BCBC8F</td></tr>
    <tr bgcolor="#BCBC8F"><td>RosyBrown </td><td>188 </td><td>143 </td><td>143</td><td> #BCBC8F</td></tr>
    <tr bgcolor="#FFFFC1"><td>RosyBrown1 </td><td>255 </td><td>193 </td><td>193</td><td> #FFFFC1</td></tr>
    <tr bgcolor="#EEEEB4"><td>RosyBrown2 </td><td>238 </td><td>180 </td><td>180</td><td> #EEEEB4</td></tr>
    <tr bgcolor="#CDCD9B"><td>RosyBrown3 </td><td>205 </td><td>155 </td><td>155</td><td> #CDCD9B</td></tr>
    <tr bgcolor="#8B8B69"><td>RosyBrown4 </td><td>139 </td><td>105 </td><td>105</td><td> #8B8B69</td></tr>
    <tr bgcolor="#414169"><td>royal blue </td><td>65 </td><td>105 </td><td>225</td><td> #414169</td></tr>
    <tr bgcolor="#414169"><td>RoyalBlue </td><td>65 </td><td>105 </td><td>225</td><td> #414169</td></tr>
    <tr bgcolor="#484876"><td>RoyalBlue1 </td><td>72 </td><td>118 </td><td>255</td><td> #484876</td></tr>
    <tr bgcolor="#43436E"><td>RoyalBlue2 </td><td>67 </td><td>110 </td><td>238</td><td> #43436E</td></tr>
    <tr bgcolor="#3A3A5F"><td>RoyalBlue3 </td><td>58 </td><td>95 </td><td>205</td><td> #3A3A5F</td></tr>
    <tr bgcolor="#272740"><td>RoyalBlue4 </td><td>39 </td><td>64 </td><td>139</td><td> #272740</td></tr>
    <tr bgcolor="#8B8B45"><td>saddle brown </td><td>139 </td><td>69 </td><td>19</td><td> #8B8B45</td></tr>
    <tr bgcolor="#8B8B45"><td>SaddleBrown </td><td>139 </td><td>69 </td><td>19</td><td> #8B8B45</td></tr>
    <tr bgcolor="#FAFA80"><td>salmon </td><td>250 </td><td>128 </td><td>114</td><td> #FAFA80</td></tr>
    <tr bgcolor="#FFFF8C"><td>salmon1 </td><td>255 </td><td>140 </td><td>105</td><td> #FFFF8C</td></tr>
    <tr bgcolor="#EEEE82"><td>salmon2 </td><td>238 </td><td>130 </td><td>98</td><td> #EEEE82</td></tr>
    <tr bgcolor="#CDCD70"><td>salmon3 </td><td>205 </td><td>112 </td><td>84</td><td> #CDCD70</td></tr>
    <tr bgcolor="#8B8B4C"><td>salmon4 </td><td>139 </td><td>76 </td><td>57</td><td> #8B8B4C</td></tr>
    <tr bgcolor="#F4F4A4"><td>sandy brown </td><td>244 </td><td>164 </td><td>96</td><td> #F4F4A4</td></tr>
    <tr bgcolor="#F4F4A4"><td>SandyBrown </td><td>244 </td><td>164 </td><td>96</td><td> #F4F4A4</td></tr>
    <tr bgcolor="#2E2E8B"><td>sea green </td><td>46 </td><td>139 </td><td>87</td><td> #2E2E8B</td></tr>
    <tr bgcolor="#2E2E8B"><td>SeaGreen </td><td>46 </td><td>139 </td><td>87</td><td> #2E2E8B</td></tr>
    <tr bgcolor="#5454FF"><td>SeaGreen1 </td><td>84 </td><td>255 </td><td>159</td><td> #5454FF</td></tr>
    <tr bgcolor="#4E4EEE"><td>SeaGreen2 </td><td>78 </td><td>238 </td><td>148</td><td> #4E4EEE</td></tr>
    <tr bgcolor="#4343CD"><td>SeaGreen3 </td><td>67 </td><td>205 </td><td>128</td><td> #4343CD</td></tr>
    <tr bgcolor="#2E2E8B"><td>SeaGreen4 </td><td>46 </td><td>139 </td><td>87</td><td> #2E2E8B</td></tr>
    <tr bgcolor="#FFFFF5"><td>seashell </td><td>255 </td><td>245 </td><td>238</td><td> #FFFFF5</td></tr>
    <tr bgcolor="#FFFFF5"><td>seashell1 </td><td>255 </td><td>245 </td><td>238</td><td> #FFFFF5</td></tr>
    <tr bgcolor="#EEEEE5"><td>seashell2 </td><td>238 </td><td>229 </td><td>222</td><td> #EEEEE5</td></tr>
    <tr bgcolor="#CDCDC5"><td>seashell3 </td><td>205 </td><td>197 </td><td>191</td><td> #CDCDC5</td></tr>
    <tr bgcolor="#8B8B86"><td>seashell4 </td><td>139 </td><td>134 </td><td>130</td><td> #8B8B86</td></tr>
    <tr bgcolor="#A0A052"><td>sienna </td><td>160 </td><td>82 </td><td>45</td><td> #A0A052</td></tr>
    <tr bgcolor="#FFFF82"><td>sienna1 </td><td>255 </td><td>130 </td><td>71</td><td> #FFFF82</td></tr>
    <tr bgcolor="#EEEE79"><td>sienna2 </td><td>238 </td><td>121 </td><td>66</td><td> #EEEE79</td></tr>
    <tr bgcolor="#CDCD68"><td>sienna3 </td><td>205 </td><td>104 </td><td>57</td><td> #CDCD68</td></tr>
    <tr bgcolor="#8B8B47"><td>sienna4 </td><td>139 </td><td>71 </td><td>38</td><td> #8B8B47</td></tr>
    <tr bgcolor="#C0C0C0"><td>silver </td><td>192 </td><td>192 </td><td>192</td><td> #C0C0C0</td></tr>
    <tr bgcolor="#8787CE"><td>sky blue </td><td>135 </td><td>206 </td><td>235</td><td> #8787CE</td></tr>
    <tr bgcolor="#8787CE"><td>SkyBlue </td><td>135 </td><td>206 </td><td>235</td><td> #8787CE</td></tr>
    <tr bgcolor="#8787CE"><td>SkyBlue1 </td><td>135 </td><td>206 </td><td>255</td><td> #8787CE</td></tr>
    <tr bgcolor="#7E7EC0"><td>SkyBlue2 </td><td>126 </td><td>192 </td><td>238</td><td> #7E7EC0</td></tr>
    <tr bgcolor="#6C6CA6"><td>SkyBlue3 </td><td>108 </td><td>166 </td><td>205</td><td> #6C6CA6</td></tr>
    <tr bgcolor="#4A4A70"><td>SkyBlue4 </td><td>74 </td><td>112 </td><td>139</td><td> #4A4A70</td></tr>
    <tr bgcolor="#6A6A5A"><td>slate blue </td><td>106 </td><td>90 </td><td>205</td><td> #6A6A5A</td></tr>
    <tr bgcolor="#707080"><td>slate gray </td><td>112 </td><td>128 </td><td>144</td><td> #707080</td></tr>
    <tr bgcolor="#707080"><td>slate grey </td><td>112 </td><td>128 </td><td>144</td><td> #707080</td></tr>
    <tr bgcolor="#6A6A5A"><td>SlateBlue </td><td>106 </td><td>90 </td><td>205</td><td> #6A6A5A</td></tr>
    <tr bgcolor="#83836F"><td>SlateBlue1 </td><td>131 </td><td>111 </td><td>255</td><td> #83836F</td></tr>
    <tr bgcolor="#7A7A67"><td>SlateBlue2 </td><td>122 </td><td>103 </td><td>238</td><td> #7A7A67</td></tr>
    <tr bgcolor="#696959"><td>SlateBlue3 </td><td>105 </td><td>89 </td><td>205</td><td> #696959</td></tr>
    <tr bgcolor="#47473C"><td>SlateBlue4 </td><td>71 </td><td>60 </td><td>139</td><td> #47473C</td></tr>
    <tr bgcolor="#707080"><td>SlateGray </td><td>112 </td><td>128 </td><td>144</td><td> #707080</td></tr>
    <tr bgcolor="#C6C6E2"><td>SlateGray1 </td><td>198 </td><td>226 </td><td>255</td><td> #C6C6E2</td></tr>
    <tr bgcolor="#B9B9D3"><td>SlateGray2 </td><td>185 </td><td>211 </td><td>238</td><td> #B9B9D3</td></tr>
    <tr bgcolor="#9F9FB6"><td>SlateGray3 </td><td>159 </td><td>182 </td><td>205</td><td> #9F9FB6</td></tr>
    <tr bgcolor="#6C6C7B"><td>SlateGray4 </td><td>108 </td><td>123 </td><td>139</td><td> #6C6C7B</td></tr>
    <tr bgcolor="#707080"><td>SlateGrey </td><td>112 </td><td>128 </td><td>144</td><td> #707080</td></tr>
    <tr bgcolor="#FFFFFA"><td>snow </td><td>255 </td><td>250 </td><td>250</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#FFFFFA"><td>snow1 </td><td>255 </td><td>250 </td><td>250</td><td> #FFFFFA</td></tr>
    <tr bgcolor="#EEEEE9"><td>snow2 </td><td>238 </td><td>233 </td><td>233</td><td> #EEEEE9</td></tr>
    <tr bgcolor="#CDCDC9"><td>snow3 </td><td>205 </td><td>201 </td><td>201</td><td> #CDCDC9</td></tr>
    <tr bgcolor="#8B8B89"><td>snow4 </td><td>139 </td><td>137 </td><td>137</td><td> #8B8B89</td></tr>
    <tr bgcolor="#0000FF"><td>spring green </td><td>0 </td><td>255 </td><td>127</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000FF"><td>SpringGreen </td><td>0 </td><td>255 </td><td>127</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000FF"><td>SpringGreen1 </td><td>0 </td><td>255 </td><td>127</td><td> #0000FF</td></tr>
    <tr bgcolor="#0000EE"><td>SpringGreen2 </td><td>0 </td><td>238 </td><td>118</td><td> #0000EE</td></tr>
    <tr bgcolor="#0000CD"><td>SpringGreen3 </td><td>0 </td><td>205 </td><td>102</td><td> #0000CD</td></tr>
    <tr bgcolor="#00008B"><td>SpringGreen4 </td><td>0 </td><td>139 </td><td>69</td><td> #00008B</td></tr>
    <tr bgcolor="#464682"><td>steel blue </td><td>70 </td><td>130 </td><td>180</td><td> #464682</td></tr>
    <tr bgcolor="#464682"><td>SteelBlue </td><td>70 </td><td>130 </td><td>180</td><td> #464682</td></tr>
    <tr bgcolor="#6363B8"><td>SteelBlue1 </td><td>99 </td><td>184 </td><td>255</td><td> #6363B8</td></tr>
    <tr bgcolor="#5C5CAC"><td>SteelBlue2 </td><td>92 </td><td>172 </td><td>238</td><td> #5C5CAC</td></tr>
    <tr bgcolor="#4F4F94"><td>SteelBlue3 </td><td>79 </td><td>148 </td><td>205</td><td> #4F4F94</td></tr>
    <tr bgcolor="#363664"><td>SteelBlue4 </td><td>54 </td><td>100 </td><td>139</td><td> #363664</td></tr>
    <tr bgcolor="#D2D2B4"><td>tan </td><td>210 </td><td>180 </td><td>140</td><td> #D2D2B4</td></tr>
    <tr bgcolor="#FFFFA5"><td>tan1 </td><td>255 </td><td>165 </td><td>79</td><td> #FFFFA5</td></tr>
    <tr bgcolor="#EEEE9A"><td>tan2 </td><td>238 </td><td>154 </td><td>73</td><td> #EEEE9A</td></tr>
    <tr bgcolor="#CDCD85"><td>tan3 </td><td>205 </td><td>133 </td><td>63</td><td> #CDCD85</td></tr>
    <tr bgcolor="#8B8B5A"><td>tan4 </td><td>139 </td><td>90 </td><td>43</td><td> #8B8B5A</td></tr>
    <tr bgcolor="#000080"><td>teal </td><td>0 </td><td>128 </td><td>128</td><td> #000080</td></tr>
    <tr bgcolor="#D8D8BF"><td>thistle </td><td>216 </td><td>191 </td><td>216</td><td> #D8D8BF</td></tr>
    <tr bgcolor="#FFFFE1"><td>thistle1 </td><td>255 </td><td>225 </td><td>255</td><td> #FFFFE1</td></tr>
    <tr bgcolor="#EEEED2"><td>thistle2 </td><td>238 </td><td>210 </td><td>238</td><td> #EEEED2</td></tr>
    <tr bgcolor="#CDCDB5"><td>thistle3 </td><td>205 </td><td>181 </td><td>205</td><td> #CDCDB5</td></tr>
    <tr bgcolor="#8B8B7B"><td>thistle4 </td><td>139 </td><td>123 </td><td>139</td><td> #8B8B7B</td></tr>
    <tr bgcolor="#FFFF63"><td>tomato </td><td>255 </td><td>99 </td><td>71</td><td> #FFFF63</td></tr>
    <tr bgcolor="#FFFF63"><td>tomato1 </td><td>255 </td><td>99 </td><td>71</td><td> #FFFF63</td></tr>
    <tr bgcolor="#EEEE5C"><td>tomato2 </td><td>238 </td><td>92 </td><td>66</td><td> #EEEE5C</td></tr>
    <tr bgcolor="#CDCD4F"><td>tomato3 </td><td>205 </td><td>79 </td><td>57</td><td> #CDCD4F</td></tr>
    <tr bgcolor="#8B8B36"><td>tomato4 </td><td>139 </td><td>54 </td><td>38</td><td> #8B8B36</td></tr>
    <tr bgcolor="#4040E0"><td>turquoise </td><td>64 </td><td>224 </td><td>208</td><td> #4040E0</td></tr>
    <tr bgcolor="#0000F5"><td>turquoise1 </td><td>0 </td><td>245 </td><td>255</td><td> #0000F5</td></tr>
    <tr bgcolor="#0000E5"><td>turquoise2 </td><td>0 </td><td>229 </td><td>238</td><td> #0000E5</td></tr>
    <tr bgcolor="#0000C5"><td>turquoise3 </td><td>0 </td><td>197 </td><td>205</td><td> #0000C5</td></tr>
    <tr bgcolor="#000086"><td>turquoise4 </td><td>0 </td><td>134 </td><td>139</td><td> #000086</td></tr>
    <tr bgcolor="#EEEE82"><td>violet </td><td>238 </td><td>130 </td><td>238</td><td> #EEEE82</td></tr>
    <tr bgcolor="#D0D020"><td>violet red </td><td>208 </td><td>32 </td><td>144</td><td> #D0D020</td></tr>
    <tr bgcolor="#D0D020"><td>VioletRed </td><td>208 </td><td>32 </td><td>144</td><td> #D0D020</td></tr>
    <tr bgcolor="#FFFF3E"><td>VioletRed1 </td><td>255 </td><td>62 </td><td>150</td><td> #FFFF3E</td></tr>
    <tr bgcolor="#EEEE3A"><td>VioletRed2 </td><td>238 </td><td>58 </td><td>140</td><td> #EEEE3A</td></tr>
    <tr bgcolor="#CDCD32"><td>VioletRed3 </td><td>205 </td><td>50 </td><td>120</td><td> #CDCD32</td></tr>
    <tr bgcolor="#8B8B22"><td>VioletRed4 </td><td>139 </td><td>34 </td><td>82</td><td> #8B8B22</td></tr>
    <tr bgcolor="#F5F5DE"><td>wheat </td><td>245 </td><td>222 </td><td>179</td><td> #F5F5DE</td></tr>
    <tr bgcolor="#FFFFE7"><td>wheat1 </td><td>255 </td><td>231 </td><td>186</td><td> #FFFFE7</td></tr>
    <tr bgcolor="#EEEED8"><td>wheat2 </td><td>238 </td><td>216 </td><td>174</td><td> #EEEED8</td></tr>
    <tr bgcolor="#CDCDBA"><td>wheat3 </td><td>205 </td><td>186 </td><td>150</td><td> #CDCDBA</td></tr>
    <tr bgcolor="#8B8B7E"><td>wheat4 </td><td>139 </td><td>126 </td><td>102</td><td> #8B8B7E</td></tr>
    <tr bgcolor="#FFFFFF"><td>white </td><td>255 </td><td>255 </td><td>255</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#F5F5F5"><td>white smoke </td><td>245 </td><td>245 </td><td>245</td><td> #F5F5F5</td></tr>
    <tr bgcolor="#F5F5F5"><td>WhiteSmoke </td><td>245 </td><td>245 </td><td>245</td><td> #F5F5F5</td></tr>
    <tr bgcolor="#FFFFFF"><td>yellow </td><td>255 </td><td>255 </td><td>0</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#9A9ACD"><td>yellow green </td><td>154 </td><td>205 </td><td>50</td><td> #9A9ACD</td></tr>
    <tr bgcolor="#FFFFFF"><td>yellow1 </td><td>255 </td><td>255 </td><td>0</td><td> #FFFFFF</td></tr>
    <tr bgcolor="#EEEEEE"><td>yellow2 </td><td>238 </td><td>238 </td><td>0</td><td> #EEEEEE</td></tr>
    <tr bgcolor="#CDCDCD"><td>yellow3 </td><td>205 </td><td>205 </td><td>0</td><td> #CDCDCD</td></tr>
    <tr bgcolor="#8B8B8B"><td>yellow4 </td><td>139 </td><td>139 </td><td>0</td><td> #8B8B8B</td></tr>
    <tr bgcolor="#9A9ACD"><td>YellowGreen </td><td>154 </td><td>205 </td><td>50</td><td> #9A9ACD</td></tr>
    </tbody></table>
</details>

> 설정값을 올바르게 입력하지 않을 경우 기본 설정이 적용됩니다.
> 단축키는 인게임에서 사용하는 단축키와 겹치지 않도록 주의해주세요.

## 주의사항

- 오버레이 기능 및 단축키는 `창모드`, `전체창모드`에서만 적용됩니다!
- 해당 프로그램은 Windows에 맞게 제작되었으며 다른 운영체제에서의 작동은 알 수 없습니다.
