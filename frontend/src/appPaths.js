class AppPaths {
    get login() {
        return "/login"
    }
    get register() {
        return "/register"
    }
    get dashboard() {
        return "/dashboard"
    }
    get termsOfService() {
        return "/terms-of-service"
    }
    get userProfile(){
        return "/user-profile"
    }
}

const appPaths = new AppPaths()

export default appPaths