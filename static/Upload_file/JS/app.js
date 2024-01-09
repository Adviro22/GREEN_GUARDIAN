var size = 400;
var canvas = document.getElementById("canvas");
var tow_canvas = document.getElementById("tow_canvas");
var ctx = canvas.getContext("2d");
var modelo = null;
var input = document.getElementById("imagen");
let respuesta;
let $cultivo = $("#cultivo").val();
let resultado_plaga = '';

// async function cambiarModelo() {
//   console.log($cultivo)
//   const nuevaRutaModelo = `/static/Upload_file/Model${$cultivo}/model.json`;
//   console.log("Cargando modelo...");
//   modelo = await tf.loadLayersModel(nuevaRutaModelo);
//   console.log("Modelo cargado", modelo);
// }

  async function cambiarModelo() {
    let $cultivo2 = $("#cultivo").val();
    console.log($cultivo2)
    let nuevaRutaModelo = `/static/Upload_file/Model${$cultivo2}/model.json`;
    console.log("Cargando modelo...");
    modelo = await tf.loadLayersModel(nuevaRutaModelo);
    console.log("Modelo cargado", modelo);
  }

  window.onload = cambiarModelo;

function processImage() {
  var img = new Image();
  img.src = URL.createObjectURL(input.files[0]);
  img.onload = function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0, size, size, 0, 0, size, size);
    predecir();
  };
}
setInterval(processImage, 1000);

function predecir() {
  if (modelo != null) {
    resample_single(canvas, 100, 100, tow_canvas);

    //Hacer la predicción
    var ctx2 = tow_canvas.getContext("2d");
    var imgData = ctx2.getImageData(0, 0, 100, 100);

    var arr = [];
    var arr100 = [];

    for (var p = 0; p < imgData.data.length; p += 4) {
      var rojo = imgData.data[p] / 255;
      var verde = imgData.data[p + 1] / 255;
      var azul = imgData.data[p + 2] / 255;

      var gris = (rojo + verde + azul) / 3;

      arr100.push([gris]);
      if (arr100.length == 100) {
        arr.push(arr100);
        arr100 = [];
      }
    }

    arr = [arr];

    var tensor = tf.tensor4d(arr);
    var resultado = modelo.predict(tensor).dataSync();
    let $cultivo3 = $("#cultivo").val();
    console.log(resultado)
    if ($cultivo3 == 1) {
      if (resultado >= 0.40) {
        respuesta = 'PLANTA INFECTADA';
        resultado_plaga = `Limpieza física: Usa un cepillo suave, hisopo de algodón o una corriente de agua para eliminar manualmente las cochinillas de las hojas y tallos. Este método puede ser eficaz para tratar infestaciones leves.

        Jabón insecticida: Mezcla agua con unas gotas de jabón insecticida suave y rocía la solución sobre las cochinillas. El jabón sofoca a los insectos y ayuda a controlar la infestación.
        `
      } else {
        respuesta = 'PLANTA SANA';
        resultado_plaga = 'Guanabana en buen estado, agregar abono y abundante Agua'
      }
    } else {
      if (resultado >= 0.45) {
        respuesta = 'PLANTA INFECTADA';
        resultado_plaga = `Fungicidas o insecticidas específicos: En caso de enfermedades específicas o infestaciones de insectos, considera el uso de productos químicos específicos según las recomendaciones de un profesional de la jardinería o agricultura.
        Limpieza física: Usa un cepillo de dientes suave o un hisopo de algodón empapado en alcohol para eliminar las cochinillas de las hojas y tallos.

        Jabón insecticida: Aplica un jabón insecticida o una solución de agua con unas gotas de detergente suave para controlar las cochinillas. Esto ayuda a sofocar y matar a los insectos.
        `
      } else {
        respuesta = 'PLANTA SANA';
        resultado_plaga = 'Carambola en buen estado, agregar abono y abundante Agua'
      }
    } console.log(resultado)
  }
}

$("#FormCultivo").submit((e) => {
  const csrftoken = $("input[name=csrfmiddlewaretoken]").val();
  e.preventDefault();
  const formData = new FormData();
  formData.append("imagen", input.files[0]);
  formData.append("respuesta", respuesta);
  formData.append("cultivo", $cultivo);
  formData.append("resultado", resultado_plaga);

  $.ajax({
    type: "POST",
    url: "/save_result/",
    contentType: false,
    processData: false,
    data: formData,
    headers: { "X-CSRFToken": csrftoken },
    success: function (result) {
      Swal.fire({
        title: "Respuesta ",
        text: result.message,
        confirmButtonText:
          '<a style="text-decoration: none; color:  white; font-size: 20px" href="/show-result/">Ok</a>',
      });
    },
  });
  return false;
});

function MostrarResultado(respuesta) {
  var formData = new FormData();
  formData.append("respuesta", respuesta);
  formData.append("imagen", URL.createObjectURL(input.files[0]));

  fetch("/saveResult", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error al enviar la solicitud:", error);
    });

  //Borar Canvas
  var ctx = canvas.getContext("2d");
  var ctx2 = tow_canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx2.clearRect(0, 0, tow_canvas.width, tow_canvas.height);

  // Mostrar la alerta
  Swal.fire({
    title: "El resultado es ",
    imageUrl: URL.createObjectURL(input.files[0]),
    imageAlt: "The uploaded picture",
    text: respuesta,
  });
}

/**
 * Hermite resize - fast image resize/resample using Hermite filter. 1 cpu version!
 *
 * @param {HtmlElement} canvas
 * @param {int} width
 * @param {int} height
 * @param {boolean} resize_canvas if true, canvas will be resized. Optional.
 * Cambiado por RT, resize canvas ahora es donde se pone el chiqitillllllo
 */
function resample_single(canvas, width, height, resize_canvas) {
  var width_source = canvas.width;
  var height_source = canvas.height;
  width = Math.round(width);
  height = Math.round(height);

  var ratio_w = width_source / width;
  var ratio_h = height_source / height;
  var ratio_w_half = Math.ceil(ratio_w / 2);
  var ratio_h_half = Math.ceil(ratio_h / 2);

  var ctx = canvas.getContext("2d");
  var ctx2 = resize_canvas.getContext("2d");
  var img = ctx.getImageData(0, 0, width_source, height_source);
  var img2 = ctx2.createImageData(width, height);
  var data = img.data;
  var data2 = img2.data;

  for (var j = 0; j < height; j++) {
    for (var i = 0; i < width; i++) {
      var x2 = (i + j * width) * 4;
      var weight = 0;
      var weights = 0;
      var weights_alpha = 0;
      var gx_r = 0;
      var gx_g = 0;
      var gx_b = 0;
      var gx_a = 0;
      var center_y = (j + 0.5) * ratio_h;
      var yy_start = Math.floor(j * ratio_h);
      var yy_stop = Math.ceil((j + 1) * ratio_h);
      for (var yy = yy_start; yy < yy_stop; yy++) {
        var dy = Math.abs(center_y - (yy + 0.5)) / ratio_h_half;
        var center_x = (i + 0.5) * ratio_w;
        var w0 = dy * dy;
        var xx_start = Math.floor(i * ratio_w);
        var xx_stop = Math.ceil((i + 1) * ratio_w);
        for (var xx = xx_start; xx < xx_stop; xx++) {
          var dx = Math.abs(center_x - (xx + 0.5)) / ratio_w_half;
          var w = Math.sqrt(w0 + dx * dx);
          if (w >= 1) {
            //pixel too far
            continue;
          }
          //hermite filter
          weight = 2 * w * w * w - 3 * w * w + 1;
          var pos_x = 4 * (xx + yy * width_source);
          //alpha
          gx_a += weight * data[pos_x + 3];
          weights_alpha += weight;
          //colors
          if (data[pos_x + 3] < 255) weight = (weight * data[pos_x + 3]) / 250;
          gx_r += weight * data[pos_x];
          gx_g += weight * data[pos_x + 1];
          gx_b += weight * data[pos_x + 2];
          weights += weight;
        }
      }
      data2[x2] = gx_r / weights;
      data2[x2 + 1] = gx_g / weights;
      data2[x2 + 2] = gx_b / weights;
      data2[x2 + 3] = gx_a / weights_alpha;
    }
  }

  ctx2.putImageData(img2, 0, 0);
}
