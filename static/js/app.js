// set up basic variables for app

const record = document.querySelector('.record');
const stop = document.querySelector('.stop');
const soundClips = document.querySelector('.sound-clips');

// disable stop button while not recording

stop.disabled = true;

// visualiser setup - create web audio api context and canvas

let audioCtx;
//main block for doing the audio recording

if (navigator.mediaDevices.getUserMedia) {
  console.log('getUserMedia supported.');
  
  const constraints = { audio: true };
  let chunks = [];
  
  let onSuccess = function(stream) {
    let blob;
    const mediaRecorder = new MediaRecorder(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    }

    stop.onclick = function() {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";
      record.style.color = "";
      // mediaRecorder.requestData();

      stop.disabled = true;
      record.disabled = false;
    }

    mediaRecorder.onstop = function(e) {
      console.log("data available after MediaRecorder.stop() called.");

      const clipName = prompt('Enter a name for your sound clip?','My unnamed clip');

    //   const clipContainer = document.createElement('article');
    //   const clipLabel = document.createElement('p');
      const audio = document.createElement('audio');
    //   const deleteButton = document.createElement('button');

    //   clipContainer.classList.add('clip');
    //   audio.setAttribute('controls', '');
    //   deleteButton.textContent = 'Delete';
    //   deleteButton.className = 'delete';

    //   if(clipName === null) {
    //     clipLabel.textContent = 'My unnamed clip';
    //   } else {
    //     clipLabel.textContent = clipName;
    //   }

    //   clipContainer.appendChild(audio);
    //   clipContainer.appendChild(clipLabel);
    //   clipContainer.appendChild(deleteButton);
    //   soundClips.appendChild(clipContainer);

      audio.controls = true;
      blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
      chunks = [];
      const audioURL = window.URL.createObjectURL(blob);
      console.log(audioURL);
      audio.src = audioURL;
      console.log("recorder stopped");

      var form_data = new FormData()
      form_data.append('file', blob)
      form_data.append('filename', 'test.wav')

      console.log(form_data)
      $.ajax({
        type : 'POST',
        url : "/receive",
        contentType : false,
        processData : false,
        data : form_data,
        success : function(data) {
          $("video").show();
         },
      })
    //   const audio_ = new Audio(audioURL);
    //   audio_.play();

    //   deleteButton.onclick = function(e) {
    //     let evtTgt = e.target;
    //     evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
    //   }

    //   clipLabel.onclick = function() {
    //     const existingName = clipLabel.textContent;
    //     const newClipName = prompt('Enter a new name for your sound clip?');
    //     if(newClipName === null) {
    //       clipLabel.textContent = existingName;
    //     } else {
    //       clipLabel.textContent = newClipName;
    //     }
    //   }
    }

    mediaRecorder.ondataavailable = function(e) {
      console.log("data available now...")
      chunks.push(e.data);
    }
  }

  let onError = function(err) {
    console.log('The following error occured: ' + err);
  }

  navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);

} else {
   console.log('getUserMedia not supported on your browser!');
}