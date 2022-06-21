// // set up basic variables for app

// const record = document.querySelector('.record');
// const stop = document.querySelector('.stop');
// const soundClips = document.querySelector('.sound-clips');

// // disable stop button while not recording

// stop.disabled = true;

// // visualiser setup - create web audio api context and canvas

// let audioCtx;
// //main block for doing the audio recording

// if (navigator.mediaDevices.getUserMedia) {
//   console.log('getUserMedia supported.');
  
//   const constraints = { audio: true };
//   let chunks = [];
  
//   let onSuccess = function(stream) {
//     let blob;
//     const mediaRecorder = new MediaRecorder(stream);

//     record.onclick = function() {
//       mediaRecorder.start();
//       console.log(mediaRecorder.state);
//       console.log("recorder started");
//       record.style.background = "red";

//       stop.disabled = false;
//       record.disabled = true;
//     }

//     stop.onclick = function() {
//       mediaRecorder.stop();
//       console.log(mediaRecorder.state);
//       console.log("recorder stopped");
//       record.style.background = "";
//       record.style.color = "";
//       // mediaRecorder.requestData();

//       stop.disabled = true;
//       record.disabled = false;
//     }

//     mediaRecorder.onstop = function(e) {
//       console.log("data available after MediaRecorder.stop() called.");

//       const clipName = prompt('Enter a name for your sound clip?','My unnamed clip');

//       const clipContainer = document.createElement('article');
//       const clipLabel = document.createElement('p');
//       const audio = document.createElement('audio');
//       const anchor = document.createElement('a');
//       const deleteButton = document.createElement('button');

//       clipContainer.classList.add('clip');
//       audio.setAttribute('controls', '');
//       deleteButton.textContent = 'Delete';
//       anchor.textContent = 'Download';
//       deleteButton.className = 'delete';

//       if(clipName === null) {
//         clipLabel.textContent = 'My unnamed clip';
//       } else {
//         clipLabel.textContent = clipName;
//       }

//       clipContainer.appendChild(audio);
//       clipContainer.appendChild(anchor);
//       clipContainer.appendChild(clipLabel);
//       clipContainer.appendChild(deleteButton);
//       soundClips.appendChild(clipContainer);

//       audio.controls = true;
//       blob = new Blob(chunks, { 'type' : 'audio/wav; codecs=PCM' });
//       chunks = [];
//       const audioURL = window.URL.createObjectURL(blob);
//       anchor.href = audioURL;
//       anchor.download = 'text3.wav';
//       console.log(audioURL);
//       audio.src = audioURL;
//       console.log("recorder stopped");

//       var form_data = new FormData()
//       form_data.append('file', blob)
//       form_data.append('filename', 'test.wav')

//       console.log(form_data)
//       $.ajax({
//         type : 'POST',
//         url : "/receive",
//         contentType : false,
//         processData : false,
//         data : form_data,
//         success : function(data) {
//           $("video").show();
//          },
//       })
//     //   const audio_ = new Audio(audioURL);
//     //   audio_.play();

//     //   deleteButton.onclick = function(e) {
//     //     let evtTgt = e.target;
//     //     evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
//     //   }

//     //   clipLabel.onclick = function() {
//     //     const existingName = clipLabel.textContent;
//     //     const newClipName = prompt('Enter a new name for your sound clip?');
//     //     if(newClipName === null) {
//     //       clipLabel.textContent = existingName;
//     //     } else {
//     //       clipLabel.textContent = newClipName;
//     //     }
//     //   }
//     }

//     mediaRecorder.ondataavailable = function(e) {
//       console.log("data available now...")
//       chunks.push(e.data);
//     }
//   }

//   let onError = function(err) {
//     console.log('The following error occured: ' + err);
//   }

//   navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);

// } else {
//    console.log('getUserMedia not supported on your browser!');
// }


//webkitURL is deprecated but nevertheless 
// URL = window.URL || window.webkitURL;
// var gumStream;
// //stream from getUserMedia() 
// var rec;
// //Recorder.js object 
// var input;
// //MediaStreamAudioSourceNode we'll be recording 
// // shim for AudioContext when it's not avb. 
// var AudioContext = window.AudioContext || window.webkitAudioContext;
// var audioContext = new AudioContext;
// //new audio context to help us record 
// var recordButton = document.getElementById("recordButton");
// var stopButton = document.getElementById("stopButton");
// var pauseButton = document.getElementById("pauseButton");
// //add events to those 3 buttons 
// recordButton.addEventListener("click", startRecording);
// stopButton.addEventListener("click", stopRecording);
// pauseButton.addEventListener("click", pauseRecording);


// function startRecording() { console.log("recordButton clicked"); }
// /* Simple constraints object, for more advanced audio features see

// https://addpipe.com/blog/audio-constraints-getusermedia/ */

// var constraints = {
//     audio: true,
//     video: false
// } 
// /* Disable the record button until we get a success or fail from getUserMedia() */

// recordButton.disabled = true;
// stopButton.disabled = false;
// pauseButton.disabled = false

// /* We're using the standard promise based getUserMedia()

// https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

// navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
//     console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 
//     /* assign to gumStream for later use */
//     gumStream = stream;
//     /* use the stream */
//     input = audioContext.createMediaStreamSource(stream);
//     /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
//     rec = new Recorder(input, {
//         numChannels: 1
//     }) 
//     //start the recording process 
//     rec.record()
//     console.log("Recording started");
// }).catch(function(err) {
//     //enable the record button if getUserMedia() fails 
//     recordButton.disabled = false;
//     stopButton.disabled = true;
//     pauseButton.disabled = true
// });


// function pauseRecording() {
//   console.log("pauseButton clicked rec.recording=", rec.recording);
//   if (rec.recording) {
//       //pause 
//       rec.stop();
//       pauseButton.innerHTML = "Resume";
//   } else {
//       //resume 
//       rec.record()
//       pauseButton.innerHTML = "Pause";
//   }
// }

// function createDownloadLink(blob) {
//   var url = URL.createObjectURL(blob);
//   var au = document.createElement('audio');
//   var li = document.createElement('li');
//   var link = document.createElement('a');
//   //add controls to the <audio> element 
//   au.controls = true;
//   au.src = url;
//   //link the a element to the blob 
//   link.href = url;
//   link.download = new Date().toISOString() + '.wav';
//   link.innerHTML = link.download;
//   //add the new audio and a elements to the li element 
//   li.appendChild(au);
//   li.appendChild(link);
//   //add the li element to the ordered list 
//   recordingsList.appendChild(li);
// }

// function stopRecording() {
//   console.log("stopButton clicked");
//   //disable the stop button, enable the record too allow for new recordings 
//   stopButton.disabled = true;
//   recordButton.disabled = false;
//   pauseButton.disabled = true;
//   //reset button just in case the recording is stopped while paused 
//   pauseButton.innerHTML = "Pause";
//   //tell the recorder to stop the recording 
//   rec.stop(); //stop microphone access 
//   gumStream.getAudioTracks()[0].stop();
//   //create the wav blob and pass it on to createDownloadLink 
//   rec.exportWAV(createDownloadLink);
// }





function runSpeechRecognition() {
  // get output div reference
  var output = document.getElementById("output");
  // get action element reference
  var action = document.getElementById("action");
      // new speech recognition object
      var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
      var recognition = new SpeechRecognition();
  
      // This runs when the speech recognition service starts
      recognition.onstart = function() {
          action.innerHTML = "<small>listening, please speak...</small>";
      };
      
      recognition.onspeechend = function() {
          action.innerHTML = "<small>stopped listening, hope you are done...</small>";
          recognition.stop();
      }
    
      // This runs when the speech recognition service returns result
      recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;
        var confidence = event.results[0][0].confidence;
        console.log(transcript)
          var form_data = new FormData()
          form_data.append('text', transcript)
          // form_data.append('filename', 'test.wav')
    
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
          output.innerHTML = "<b>Text:</b> " + transcript + "<br/> <b>Confidence:</b> " + confidence*100+"%";
          output.classList.remove("hide");
      };
    
       // start recognition
       recognition.start();
}