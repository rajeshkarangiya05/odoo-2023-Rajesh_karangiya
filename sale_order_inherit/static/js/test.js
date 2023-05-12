var input = document.getElementById('avatar');
if(input) {
  input.addEventListener('change', function () {
    getUploadImageUrl(this);
  });
}

function getUploadImageUrl(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      document.getElementById('avatar_preview').setAttribute('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
}