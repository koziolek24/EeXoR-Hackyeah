import {sessionSettings} from "@/app/lib/sessionSettings";
import {NextResponse} from "next/server";


export function logout(response: NextResponse) {
    response.cookies.delete(sessionSettings.cookieName);
}