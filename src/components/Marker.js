import React from 'react'
import { Marker as MapMarker } from 'react-map-gl'

class Marker extends React.Component {
  render() {
    return (
      <MapMarker
        latitude={this.props.lat}
        longitude={this.props.lon}
      >
        <div className="map-marker">
          {this.props.additionalProperties[7].value}
        </div>
      </MapMarker>
    )
  }
}

export default Marker
