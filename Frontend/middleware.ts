import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { cookies } from "next/headers";


export const sessionSettings = {
    cookieName: 'UID',
};

export async function middleware(request: NextRequest) {
    const cookieStore = cookies();
    if(cookieStore.has(sessionSettings.cookieName))
    {
        const response = NextResponse.next();
        if (new URL(request.url).pathname == "/dashboard/logout") {
            response.cookies.delete(sessionSettings.cookieName);
        }
        return response;
    }

    let formData;
    try {
        formData = await request.formData();
    } catch (e) {
        return NextResponse.redirect(new URL("/", request.url));
    }

    if (new URL(request.url).pathname == "/dashboard" && request.method === "POST" && formData.has("login")) {
        const login = formData.get("login")?.toString();
        formData = new FormData();
        formData.set("handle", login);
        const res = await fetch(`${process.env.API_URL}/login/`, {
            method: "POST",
            body: formData,
        });

        console.log(res.status, res.json());

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