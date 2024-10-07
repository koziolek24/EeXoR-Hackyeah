

export default function Home() {
  return (
      <main>
          <br/>
        <form method="post" action="/login">
          <input type="text" placeholder="Login" name="login" /><br/><br/>
          <input type="submit" value="Login" />
        </form>
      </main>
  );
}
