import axios from 'axios'
import { ToastService } from './buefy'

const ApiService = {
  init(baseURL) {
    axios.defaults.baseURL = baseURL

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    axios.interceptors.response.use(
      (response) => response.data,
      (err) => {
        let msg = ''

        try {
          switch (err.response.status) {
            case 500:
            case 404:
              msg = err.response.data.detail || 'Something went wrong'
              break
            case null:
              msg = 'Please check your internet connection'
              break
            default:
              for (let e in err.response.data) {
                const o = err.response.data[e]
                msg += (Array.isArray(o) && o[0]) || o + '<br/>'
                break
              }
              break
          }
        } catch {
          if (err.response == null) msg = 'Unable to connect to database'
        }

        msg = 'Error<br> ' + msg

        ToastService.open(msg, {
          type: 'is-danger',
        })

        return Promise.reject(err)
      }
    )
  },

  get(resource) {
    return axios.get(resource)
  },

  post(resource, data) {
    return axios.post(resource, data)
  },

  put(resource, data) {
    return axios.put(resource, data)
  },

  patch(resource, data) {
    return axios.patch(resource, data)
  },

  options(resource) {
    return axios.options(resource)
  },

  delete(resource) {
    return axios.delete(resource)
  },

  request(data) {
    return axios(data)
  },
}

export default ApiService
