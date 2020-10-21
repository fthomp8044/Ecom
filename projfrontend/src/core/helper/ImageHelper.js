import React from 'react';

const ImageHelper = () => {
  const imageurl = product ? product.image
  : `http://127.0.0.1:8000/media/images/00-cover-back_bUwmUW1.jpg`
  return (
    <div className="rounded border border-success p-2">
      <img src={imageurl}
      style={{ maxHeight:"100%", maxWidth:"100%" }}
      className="mb-3 rounded"
      alt="" />
    </div>
  )
}

export default ImageHelper;
