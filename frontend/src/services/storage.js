const TOKEN_KEY = 'biserici-inlemnite_token'

export default {
  getToken() {
    return localStorage.getItem(TOKEN_KEY)
  },

  saveToken(accessToken) {
    localStorage.setItem(TOKEN_KEY, accessToken)
  },

  removeToken() {
    localStorage.removeItem(TOKEN_KEY)
  },
}
