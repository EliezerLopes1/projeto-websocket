import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCaption,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

export function Room() {
  return (
    <div className="flex min-h-screen">
      <div className="bg-[#F0F0F0] w-full flex items-center justify-center">
        <div className="bg-[#016B94]/70 w-1/2 h-1/2 rounded-md">
          <div>
            <Table>
              <TableHeader className="">
                <div className="flex justify-between items-center m-2">
                  <TableCaption className="text-black text-2xl">
                    Grupos
                  </TableCaption>
                  <Popover>
                    <PopoverTrigger
                      render={<Button variant="outline" className="cursor-pointer">Ação</Button>}
                    />
                    <PopoverContent className="w-40 flex flex-col gap-1">
                      <Button variant="ghost" className="justify-start cursor-pointer">
                        Cria uma Sala
                      </Button>
                      <Button variant="ghost" className="justify-start cursor-pointer">
                        Entrar em uma Sala
                      </Button>
                    </PopoverContent>
                  </Popover>
                </div>
              </TableHeader>
              <hr className="border-black w-full" />
              <TableBody>
                <TableRow></TableRow>
              </TableBody>
            </Table>
          </div>
        </div>
      </div>
    </div>
  );
}
