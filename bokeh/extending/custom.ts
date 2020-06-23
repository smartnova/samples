// https://github.com/bokeh/bokeh/issues/9587 の議論が大変、参考になった。ドキュメントが大幅に間違っている？

import {HTMLBox, HTMLBoxView} from "models/layouts/html_box"

import {div} from "core/dom"
import * as p from "core/properties"
import { Slider } from "models/widgets/slider"

export class CustomView extends HTMLBoxView {
  model: Custom

  connect_signals(): void {
    super.connect_signals()
    this.connect(this.model.slider.change, () => {
      this.render()
      this.invalidate_layout()
    })
  }

  render(): void {
    super.render()
    this.el.appendChild(div({
      style: {
        padding: '2px',
        color: '#b88d8e',
        backgroundColor: '#2a3153',
      },
    }, `${this.model.text}: ${this.model.slider.value}`))
  }
}

export namespace Custom {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HTMLBox.Props & {
    slider: p.Property<Slider>
    text: p.Property<string>
  }
}

export interface Custom extends Custom.Attrs {}

export class Custom extends HTMLBox {
  properties: Custom.Props

  static init_Custom(): void {
    this.prototype.default_view = CustomView

    this.define<Custom.Props>({
      text: [ p.String ],
      slider: [ p.Instance ],
    })
  }
}
