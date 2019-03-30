#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

static int kmodule_init(void) {
        printk(KERN_INFO "Initializing this module\n");
        return 0;
}

static void kmodule_exit(void) {
        printk(KERN_INFO "Module cleanup\n");
}

module_init(kmodule_init);       
module_exit(kmodule_exit);      

MODULE_LICENSE("GPL");
