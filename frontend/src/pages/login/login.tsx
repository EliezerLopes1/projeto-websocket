import { Button } from "@/components/ui/button";
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { postLogin } from "../../services/api";

function Login() {
  const [username, setUsername] = useState("");
  const navigation = useNavigate();

  const handleSubmitLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const dadosUsuario = await postLogin(username);
      console.log("Login feito com sucesso!", dadosUsuario);
      navigation("/room");
    } catch (error) {
      console.error("Erro ao fazer login:", error);
    }
  };

  const handleLoginScreen = () => {
    navigation("/register");
  };

  return (
    <div className="flex min-h-screen">
      <div className="bg-[#F0F0F0] w-1/2 flex items-center justify-center">
        <form onSubmit={handleSubmitLogin} className="w-1/2">
          <Field>
            <FieldLabel htmlFor="input-field-username">
              Nome do Usuário
            </FieldLabel>
            <Input
              id="input-field-username"
              type="text"
              placeholder="Exemplo: Eric Twink"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <FieldDescription className="text-right">
              Não tem um usuário?
              <span
                className="cursor-pointer font-bold ml-1"
                onClick={handleLoginScreen}
              >
                Criar Conta
              </span>
            </FieldDescription>
          </Field>

          <div className="flex items-center justify-center mt-15">
            <Button
              type="submit"
              className="w-1/2 bg-[#016B94]/80 hover:bg-[#016B94]/60 cursor-pointer"
            >
              Entrar
            </Button>
          </div>
        </form>
      </div>
      <div className="bg-[#016B94]/80 w-1/2"></div>
    </div>
  );
}

export default Login;
