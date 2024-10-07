import { Patrick_Hand } from 'next/font/google'

const patrickHand = Patrick_Hand({ weight: [ "400" ], subsets: ["latin"]});

export default function Home() {
  return    <main className="vh-100">
            <div className="container py-5 h-100">
                <div className="row d-flex justify-content-center align-items-center h-100">
                  <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                      <div className="card bg-dark" style={{borderRadius: '1rem'}}>
                          <div className="card-body px-5 py-2 text-center">
                              <div className="pb-5 mt-4">
                                  <h1 className="text-white mb-3">Edu<span className={patrickHand.className} style={{fontSize: "110%"}}>X</span>oR</h1>
                                  <form action="/login" method="POST">
                                      <div className="form-floating mb-3">
                                          <input type="text" name="login" id="login" placeholder="login" className="form-control"/>
                                          <label htmlFor="login">login</label>
                                      </div>
                                      <button className="btn btn-primary btn-large w-100 px-5 py-3" type="submit">
                                          Log in
                                      </button>
                                  </form>
                                  <p className="small mt-3 mb-0 pb-lg-2">
                                      <a className="text-white-50" href="#">Register</a>
                                  </p>
                                  <p className="text-danger mb-3">Please enter valid login!</p>
                              </div>
                          </div>
                      </div>
                  </div>
                </div>
            </div>
            </main>;
}
