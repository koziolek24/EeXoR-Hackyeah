import {ReadonlyRequestCookies} from "next/dist/server/web/spec-extension/adapters/request-cookies";
import {sessionSettings} from "@/app/lib/sessionSettings";


export function verifyLogin(cookieStore: ReadonlyRequestCookies) {
    return cookieStore.has(sessionSettings.cookieName);
}