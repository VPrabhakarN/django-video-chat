const APP_ID = '5105b847a34a4b34aa7cabdf0e21e295'
const CHANNEL = 'main'
const TOKEN = '007eJxTYDii1sL2MeasZF57EN+Z1kMnp+6bZVnixP2vjPno9uoO/S8KDKaGBqZJFibmicYmiSZJQCLRPDkxKSXNINXIMNXI0jRXKT2rIZCRQYbPnZmJgREMQXwWhtzEzDwGBiYkEUMDA0MAGhQftw=='
let UID;
const client = AgoraRTC.createClient({mode : 'rtc', codec : 'vp8'})

let localTracks = []
let remoteUsers = {}

let joiAndDisplayLocalSream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `  <div class="video-container" id="user-container-${UID}">
                      <div class="username-wrapper">
                       <span class="user-name">My Name </span>
                      </div>
                      <div class="video-player" id="user-${UID}"></div>
                    </div>`

    document.getElementById('video-streams').insertAdjancentHTML('beforeend', player)

    localTracks[1].play('user-${UID}')

    await client.publish([localTracks[0], localTracks[1]])
}

