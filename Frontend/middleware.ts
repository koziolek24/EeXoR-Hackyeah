import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import {cookies} from "next/headers";

export type SessionData = {
    userId: string;
};

export const sessionSettings = {
    cookieName: 'UID',
};

export async function middleware(request: NextRequest) {
    const cookieStore = cookies();
    if(cookieStore.has(sessionSettings.cookieName))
    {
        return NextResponse.next();
    }

    const formData = await request.formData();
    if (request.method === "POST" && new URL(request.url).pathname == "/dashboard" && formData.has("login")) {
        const login = formData.get("login");
        const userId = 1; // select by  login

        const response = NextResponse.next();
        response.cookies.set(sessionSettings.cookieName, userId.toString())

        return response;
    }

    return NextResponse.redirect(new URL('/', request.url));
}

export const config = {
    matcher: "/dashboard/:p*",
};