import { Patrick_Hand } from 'next/font/google'

const patrickHand = Patrick_Hand({ weight: [ "400" ], subsets: ["latin"]});


export default function Logo({EduXor = true}) {
    return <>{ EduXor ?  "Edu" : "Ee" }<span className={patrickHand.className} style={{fontSize: "120%"}}>X</span>oR</>;
}