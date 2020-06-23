import {HTMLBoxView, HTMLBox} from "models/layouts/html_box"

import {div} from "core/dom"
import * as p from "core/properties"

export class DetailsView extends HTMLBoxView {
  /*
  connect_signals(): void {
    console.log('connect_signals')
    super.connect_signals()

    let model = <Details>this.model
    this.connect(model.description.change, () => {
      this.render()
      this.invalidate_layout()
    })
  }
  */

  render(): void {
    console.log('render...')
    super.render()

    let model = <Details>this.model
    this.el.appendChild(div({}, `${model.description}`))
    console.log('render - done')
  }
}

export namespace Details {
  export type Props = {
    description: p.Property<string>
  }
}

export class Details extends HTMLBox {
  description: string

  static init_Details(): void {
    console.log('init details...')
    this.prototype.default_view = DetailsView

    this.define<any>({
      description: [p.String]
    })
    console.log('init details done')
  }
}
